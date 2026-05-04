import pandas as pd
import numpy as np

# ------------------ cleaning kaggle social media and mental health data ------------------
# importing raw data
df = pd.read_csv('data/raw/kaggle_socialmedia_mentalhealth.csv')


# removing columns that are not needed for the analysis
df_clean = df.drop(columns=[
    'Timestamp',
    '3. Relationship Status',
    '4. Occupation Status',
    '5. What type of organizations are you affiliated with?',
    '9. How often do you find yourself using Social media without a specific purpose?',
    '10. How often do you get distracted by Social media when you are busy doing something?',
    '19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?',
    '20. On a scale of 1 to 5, how often do you face issues regarding sleep?'
])

# change collumn headings to be coding-friendly
new_column_names = {
    '1. What is your age?': 'age',
    '2. Gender': 'gender',
    '6. Do you use social media?': 'social_media_usage',
    '7. What social media platforms do you commonly use?': 'social_media_platforms',
    '8. What is the average time you spend on social media every day?': 'social_media_time',
    '11. Do you feel restless if you haven\'t used Social media in a while?': 'restless_without_social_media', 
    '12. On a scale of 1 to 5, how easily distracted are you?': 'distraction',
    '13. On a scale of 1 to 5, how much are you bothered by worries?': 'worry',
    '14. Do you find it difficult to concentrate on things?': 'concentration_difficulty',
    '15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?': 'social_comparison',
    '16. Following the previous question, how do you feel about these comparisons, generally speaking?': 'feeling_about_comparisons',
    '17. How often do you look to seek validation from features of social media?': 'seeking_validation',
    '18. How often do you feel depressed or down?': 'depression'
}

df_clean.rename(columns = new_column_names, inplace = True)

# convert the time_spent column into numeric values to be coding-friendly
# use time approximations
time_map = {
    'Less than an Hour': 0.5,
    'Between 1 and 2 hours': 1.5,
    'Between 2 and 3 hours': 2.5,
    'Between 3 and 4 hours': 3.5,
    'Between 4 and 5 hours': 4.5,
    'More than 5 hours': 6.0
}
df_clean['social_media_time'] = df_clean['social_media_time'].map(time_map)

# print(df_clean.isnull().sum()) gives 0 for all columns so ready to move on

# cleaning the names of gender as they are not coding-friendly and there are multiple for 'non-binary'
df_clean['gender'] = df_clean['gender'].str.strip().str.lower()
df_clean['gender'] = df_clean['gender'].replace({
    'nb': 'non-binary',
    'non binary': 'non-binary',
    'nonbinary': 'non-binary',
    'there are others???': 'other',
    'unsure': 'other',
})

df_clean.to_csv('data/clean/kaggle_clean.csv', index=False)

