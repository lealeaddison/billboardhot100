import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset
df = pd.read_csv("hotstuff.csv")

# cleaning artist names by removing featured artists and extra info
df['Performer'] = df['Performer'].str.replace(r'\s+\(.*?\)|feat.*', '', regex=True).str.strip()

# adding a year column for easier grouping
df['year'] = pd.to_datetime(df['WeekID']).dt.year

# Step 1: identifying the first year an artist appeared on the chart
first_year = df.groupby('Performer')['year'].min().reset_index()
first_year.columns = ['Performer', 'first_year']

# Step 2: counting unique songs per artist to classify them as one-hit wonders or superstars
song_counts = df.groupby('Performer')['Song'].nunique().reset_index()
song_counts.columns = ['Performer', 'num_songs']

# merging first year and song counts
performer_info = first_year.merge(song_counts, on='Performer')

# classifying artists based on number of unique songs
performer_info['performer_type'] = performer_info['num_songs'].apply(
    lambda x: 'One-Hit Wonder' if x == 1 else 'Superstar'
)

# counting new artists per year by type
yearly_new = performer_info.groupby(['first_year', 'performer_type'])['Performer'].count().reset_index()
yearly_new.columns = ['year', 'performer_type', 'count']

# Step 4: computing percentages of new artists each year
total_per_year = yearly_new.groupby('year')['count'].sum().reset_index()
total_per_year.columns = ['year', 'total_new_performers']

yearly_new = yearly_new.merge(total_per_year, on='year', how='left')
yearly_new['percent'] = (yearly_new['count'] / yearly_new['total_new_performers']) * 100

# creating the line plot using seaborn
plt.figure(figsize=(12,6))
sns.lineplot(data=yearly_new, x='year', y='percent', hue='performer_type', marker='o')

plt.title("Percentage of New Performers Who Become One-Hit Wonders vs. Superstars (1958–2017)")
plt.ylabel("Percentage of New Performers (%)")
plt.xlabel("Year")
plt.legend(title="Performer Type")
plt.tight_layout()
plt.show()

