import pandas as pd

# loading dataset
df = pd.read_csv("hotstuff.csv")

# cleaning artist names
df['Performer'] = (
    df['Performer']
    .str.replace(r'\s+\(.*?\)|feat.*', '', regex=True)
    .str.strip()
)

# extracting year
df['year'] = pd.to_datetime(df['WeekID'], errors='coerce').dt.year

# finding first year a performer appeared
first_year = df.groupby('Performer')['year'].min().reset_index()
first_year.columns = ['Performer', 'first_year']

# finding number of unique songs per performer
song_counts = df.groupby('Performer')['Song'].nunique().reset_index()
song_counts.columns = ['Performer', 'num_songs']

# merging data
performer_info = first_year.merge(song_counts, on='Performer')

# classifying performers
performer_info['performer_type'] = performer_info['num_songs'].apply(
    lambda x: 'One-Hit Wonder' if x == 1 else 'Superstar'
)

# counting new performers per year by type
yearly_new = (
    performer_info.groupby(['first_year', 'performer_type'])['Performer']
    .count()
    .reset_index()
)
yearly_new.columns = ['year', 'performer_type', 'count']

# finding percentages of new performers each year
total_per_year = yearly_new.groupby('year')['count'].sum().reset_index()
total_per_year.columns = ['year', 'total_new_performers']

yearly_new = yearly_new.merge(total_per_year, on='year', how='left')
yearly_new['percent'] = (yearly_new['count'] / yearly_new['total_new_performers']) * 100


# total counts
total_songs = df['Song'].nunique()
total_artists = df['Performer'].nunique()
total_chart_entries = len(df)

print(f"Total unique songs analyzed: {total_songs}")
print(f"Total unique artists analyzed: {total_artists}")
print(f"Total chart entries (including repeats): {total_chart_entries}")

# highest % of one-hit wonders
one_hit_data = yearly_new[yearly_new['performer_type'] == 'One-Hit Wonder']
max_one_hit_year = one_hit_data.loc[one_hit_data['percent'].idxmax()]
print(f"Year with highest percentage of one-hit wonders: {int(max_one_hit_year['year'])} ({max_one_hit_year['percent']:.2f}%)")

# highest % of superstars
superstar_data = yearly_new[yearly_new['performer_type'] == 'Superstar']
max_superstar_year = superstar_data.loc[superstar_data['percent'].idxmax()]
print(f"Year with highest percentage of superstars: {int(max_superstar_year['year'])} ({max_superstar_year['percent']:.2f}%)")

# decade counts — One-Hit Wonders
decade_one_hit = performer_info[performer_info['performer_type'] == 'One-Hit Wonder'].copy()
decade_one_hit['decade'] = (decade_one_hit['first_year'] // 10) * 10

decade_counts = decade_one_hit.groupby('decade')['Performer'].count().reset_index()
decade_counts.columns = ['decade', 'one_hit_wonders']
most_one_hit_decade = decade_counts.loc[decade_counts['one_hit_wonders'].idxmax()]

print(f"Decade with most one-hit wonders: {int(most_one_hit_decade['decade'])} ({most_one_hit_decade['one_hit_wonders']})")

# decade counts — Superstars
decade_superstar = performer_info[performer_info['performer_type'] == 'Superstar'].copy()
decade_superstar['decade'] = (decade_superstar['first_year'] // 10) * 10

decade_counts_superstar = decade_superstar.groupby('decade')['Performer'].count().reset_index()
decade_counts_superstar.columns = ['decade', 'superstars']
most_superstar_decade = decade_counts_superstar.loc[decade_counts_superstar['superstars'].idxmax()]

print(f"Decade with most superstars: {int(most_superstar_decade['decade'])} ({most_superstar_decade['superstars']})")
