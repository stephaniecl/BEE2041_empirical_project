import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
from scipy import stats
from datetime import datetime

# deciding on a colour code for all figures
COLOUR_MAIN   = '#6B4F8C'
COLOUR_ACCENT = '#F4845F'
FONT_TITLE    = 14
FONT_LABEL    = 11
FONT_TICK     = 9

# FIGURES FOR THE KAGGLE SOCIAL MEDIA AND MENTAL HEALTH DATA
df = pd.read_csv('data/clean/kaggle_analysis.csv')


mental_health_columns = {
    'depression':                   'Depression',
    'seeking_validation':           'Seeking Validation',
    'feeling_about_comparisons':    'Response to Social Comparison',
    'worry':                        'Worry',
    'concentration_difficulty':     'Concentration Difficulty',
    'restless_without_social_media':'Restlessness Without Social Media'
}

# Figure 1 - Correlation heatmap of social meadia time vs the mental health indicators
columns_for_heatmap = ['social_media_time'] + list(mental_health_columns.keys())
labels              = ['Daily Usage (hrs)'] + list(mental_health_columns.values())

corr_matrix = df[columns_for_heatmap].corr()
corr_matrix.columns = labels
corr_matrix.index   = labels

fig, ax = plt.subplots(figsize=(9, 7))

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    vmin=-1, vmax=1,
    linewidths=0.5,
    linecolor='white',
    annot_kws={'size': 9},
    ax=ax
)

ax.set_title(
    'Correlation Between Daily Social Media Use\nand Mental Health Indicators',
    fontsize=FONT_TITLE, fontweight='bold', pad=15
)
ax.tick_params(axis='x', labelsize=FONT_TICK, rotation=30)
ax.tick_params(axis='y', labelsize=FONT_TICK, rotation=0)

# fixing overlap on the x-axis
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', fontsize=FONT_TICK)

plt.tight_layout()
plt.savefig('output/figures/fig1_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()



# figure 2 - Scatter plot of social media use vs mental health score
x = df['social_media_time']
y = df['mental_health_score']

slope, intercept, r, p, _ = stats.linregress(x, y)
line_x = np.linspace(x.min(), x.max(), 200)
line_y = slope * line_x + intercept

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    x, y,
    alpha=0.35,
    s=40,
    color=COLOUR_MAIN,
    edgecolors='white',
    linewidths=0.4,
    label='Respondent'
)

ax.plot(
    line_x, line_y,
    color=COLOUR_ACCENT,
    linewidth=2,
    label=f'Regression line (r = {r:.2f}, p < 0.001)'
)

ax.set_xlabel('Daily Social Media Use (hours)', fontsize=FONT_LABEL)
ax.set_ylabel('Composite Mental Health Score', fontsize=FONT_LABEL)
ax.set_title(
    'Daily Social Media Use vs Composite Mental Health Score',
    fontsize=FONT_TITLE, fontweight='bold'
)
ax.legend(fontsize=FONT_TICK)
ax.tick_params(labelsize=FONT_TICK)
ax.spines[['top', 'right']].set_visible(False)

# annotate with key stats
ax.annotate(
    f'r = {r:.3f}, p < 0.001',
    xy=(0.05, 0.92), xycoords='axes fraction',
    fontsize=9, color=COLOUR_ACCENT,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLOUR_ACCENT, alpha=0.8)
)


plt.tight_layout()
plt.savefig('output/figures/fig2_scatter_regression.png', dpi=150, bbox_inches='tight')
plt.close()


# FIGURES FOR THE GOOGLE NEWS ARTICLES
df_news = pd.read_csv('data/raw/google_news_articles.csv')

df_news['date'] = pd.to_datetime(df_news['date'], errors='coerce', utc=True)
df_news['date'] = df_news['date'].dt.tz_localize(None)
df_news['month'] = df_news['date'].dt.to_period('M')

monthly_counts = df_news.groupby('month').size().reset_index(name='count')
monthly_counts['month_dt'] = monthly_counts['month'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    monthly_counts['month_dt'],
    monthly_counts['count'],
    color=COLOUR_MAIN,
    alpha=0.85,
    width=20
)

# adding the date K.G.M won the case against Meta (25/03/2026)
# however because all news items posted in march are logged for the 1st of March we will label it for then
verdict_date = datetime(2026, 3, 1)
ax.axvline(verdict_date, color=COLOUR_ACCENT, linewidth=2, linestyle='--')
ax.text(
    verdict_date, ax.get_ylim()[1] * 0.8,
    '      K.G.M. wins case\n      against Meta',
    color=COLOUR_ACCENT,
    fontsize=9,
    fontweight='bold'
)

ax.set_xlabel('Month', fontsize=11)
ax.set_ylabel('Number of Articles', fontsize=11)
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.set_title(
    'Google News Coverage: Social Media & Mental Health\nPast 12 Months',
    fontsize=13, fontweight='bold'
)
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('output/figures/fig_news_coverage.png', dpi=150, bbox_inches='tight')
plt.close()