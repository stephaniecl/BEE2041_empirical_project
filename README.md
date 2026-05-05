# Social Media and Mental Health
**“Does spending more time on social media deteriorate mental health?”**


## Motivation
This project was inspired by the lawsuit that K.G.M. placed on Meta over how the platform was ruining her mental health. On the 25th of March she won $6 million of compensation, proving that the company did cause her harm. 

This blog investigates whether the harms describedin the lawcase are detectable at scale across ordinary social media users.

Hence I look at individual data showing average social media user's survey data and then look at how the broader population has responded to the lawsuit by scraping the news headlines over the past 12 months.

## Requirements
Python 3.14.4

Install dependencies with bash:
```bash
python -m pip install pandas numpy matplotlib seaborn statsmodels scipy requests pyyaml jupyter 
```

Also install [Quarto](https://quarto.org/docs/get-started/) seperately.


## Data sources
- Kaggle dataset: https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health/data
- Google News RSS feed: scraped live from 'https://news.google.com/rss/search?q={query}&hl=en-GB&gl=GB&ceid=GB:en'


## How to replicate
1. Clone this repository

2. Download the Kaggle dataset and save to 'data/raw/kaggle_socialmedia_mentalhealth.csv'

3. Run 'python src/01_clean.py to clean the Kaggle raw data to 'data/clean/kaggle_clean.csv'

4. Run 'python src/02_analysis.py' which will save a second clean data to 'data/clean/kaggle_analysis.csv'

5. Run 'python src/04_scrape.py' to scrape the Google News RSS feed to 'data/raw/google_news_articles.csv'

**IMPORTANT: data scraped may be different to data saved in the report as new articles might have come out, changing the ratio of the 100 articles we are able to scrape over the last 12 months**

6. Run 'python src/03_figures.py' to generate all figures to 'output/figures/'

7. 'cd report && quarto render blog.qmd' which renders the blog to 'report/blog.html'




## Output
Blog: open 'report/blog.html' in a browser
Source is 'report/blog.qmd'

**Live site:** https://stephaniecl.github.io/BEE2041_empirical_project/