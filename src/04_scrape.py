import requests
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# finding the google news
query = 'social+media+mental+health'
url = f'https://news.google.com/rss/search?q={query}&hl=en-GB&gl=GB&ceid=GB:en'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
root = ET.fromstring(response.content)

# sort through articles
articles = []
for item in root.findall('./channel/item'):
    title   = item.find('title').text
    pub_date = item.find('pubDate').text
    source  = item.find('source').text if item.find('source') is not None else 'Unknown'
    link    = item.find('link').text

# sort through dates
    try:
        date = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %Z')
    except:
        date = None

    articles.append({
        'title':  title,
        'date':   date,
        'source': source,
        'link':   link
    })

# inspect data
df_news = pd.DataFrame(articles)
df_news = df_news.dropna(subset=['date'])
df_news['month'] = df_news['date'].dt.to_period('M')

print(f"Total articles found: {len(df_news)}")
print(df_news[['title', 'source', 'date']].head(10))

df_news.to_csv('data/raw/google_news_articles.csv', index=False)