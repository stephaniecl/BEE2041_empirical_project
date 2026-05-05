import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

# cleaned kaggle data
df = pd.read_csv('data/clean/kaggle_clean.csv')

# creating an overall mental health score for each individual - the average for each person over all the catogories
df['mental_health_score'] = df[[
    'distraction',
    'worry',
    'concentration_difficulty',
    'social_comparison',
    'feeling_about_comparisons',
    'seeking_validation',
    'depression'
]].mean(axis=1)




# summary statistics
summary_statistics = df[[
    'social_media_time',
    'mental_health_score',
    'depression',
    'seeking_validation',
    'feeling_about_comparisons',
    'worry',
    'concentration_difficulty',
    'restless_without_social_media'
]].describe().round(2).T[['mean', 'std', 'min', 'max']]

summary_statistics.to_csv('output/tables/summary_statistics.csv')


# finding the correlation value between social media time and mental health score
corr, p_val = stats.pearsonr(df['social_media_time'], df['mental_health_score'])

# print to see values to 3 decimal places
print("CORRELATION: Social media time vs mental health score")
print(f"Overall correlation:         {corr:.3f}")
print(f"P-value:                     {p_val:.3f}")


# ols regression to analyse the affect of social media usage on mental health independant of age and gender
model_base = smf.ols(
    'mental_health_score ~ social_media_time + age + C(gender)',
    data=df
).fit()

print("\nOLS Table")
print(model_base.summary().tables[1])

print(f"R-squared: {model_base.rsquared:.3f}")
print(f"Adjusted R-squared: {model_base.rsquared_adj:.3f}")

with open('output/tables/regression_summary.txt', 'w') as f:
    f.write(model_base.summary().tables[1].as_text())
    f.write("\n" f"R-squared: {model_base.rsquared:.3f}")
    f.write("\n" f"Adjusted R-squared: {model_base.rsquared_adj:.3f}")

# save to seperate data set
df.to_csv('data/clean/kaggle_analysis.csv', index=False)
df.len()
