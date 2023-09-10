# add your code here
import pandas as pd

# This line is what reads teh data
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# This line will create a summary 
summary = df.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count', 'points': 'points'})
summary['points'] = summary['points'].round(1)

# This line creates a csv file
summary.to_csv('data/reviews-per-country.csv')

# This prints the summary 
print(summary)

