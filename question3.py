import pandas as pd
import matplotlib.pyplot as plt
import ast
import seaborn as sns

hot_stuff = pd.read_csv('hotstuff.csv')
hot_100 = pd.read_csv('hot100_audio.csv')

hot_stuff['WeekID'] = pd.to_datetime(hot_stuff['WeekID'])


df = hot_stuff.merge(hot_100,on="SongID",how="left")


df.rename(columns={'Performer_x':'Performer'}, inplace=True)
df.drop(columns=['Song_y','Performer_y'], inplace=True)
df.rename(columns={'Song_x':'Song'}, inplace=True)
print(df.columns)


df['spotify_genre'] = df['spotify_genre'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

song_counts = df.groupby('Performer')['SongID'].nunique().reset_index()
song_counts.columns = ['Performer', 'NumSongs']

df = df.merge(song_counts, on='Performer', how='left')

df['OneHitWonder'] = df['NumSongs'] == 1

df['Year'] = pd.to_datetime(df['WeekID']).dt.year
df['Decade'] = (df['Year'] // 10) * 10

df_exploded = df.explode('spotify_genre')

df_exploded['spotify_genre'] = df_exploded['spotify_genre'].replace('', 'Unknown')

genre_map = {
    'pop': 'Pop',
    'dance': 'Pop',
    'novelty': 'Pop',
    'rock': 'Rock',
    'punk': 'Rock',
    'metal': 'Rock',
    'soft rock': 'Rock',
    'classic rock': 'Rock',
    'hip hop': 'Hip-Hop',
    'rap': 'Hip-Hop',
    'r&b': 'R&B',
    'soul': 'R&B',
    'country': 'Country',
    'jazz': 'Jazz/Blues',
    'blues': 'Jazz/Blues',
    'classical': 'Classical',
    'electro': 'Electronic',
    'edm': 'Electronic'
}

def map_broad_genre(g):
    if not isinstance(g, str):
        return 'Other'
    g = g.lower()
    for keyword, broad in genre_map.items():
        if keyword in g:
            return broad
    return 'Other'

df_exploded['BroadGenre'] = df_exploded['spotify_genre'].apply(map_broad_genre)

# -----------------------------
# 8. Pivot table: proportion of one-hit wonders by broad genre and decade
# -----------------------------
genre_decade_broad = (
    df_exploded.groupby(['BroadGenre', 'Decade'])['OneHitWonder']
    .mean()
    .reset_index()
    .pivot(index='BroadGenre', columns='Decade', values='OneHitWonder')
)

# -----------------------------
# 9. Plot heatmap (broad genres)
# -----------------------------
genre_decade_percent = genre_decade_broad * 100

plt.figure(figsize=(12,6))

# Plot each genre
for genre in genre_decade_percent.index:
    plt.plot(
        genre_decade_percent.columns, 
        genre_decade_percent.loc[genre], 
        marker='o', 
        label=genre
    )

plt.xlabel("Decade")
plt.ylabel("Proportion of One-Hit Wonders (%)")
plt.title("One-Hit Wonder Trends by Broad Genre Over Decades")
plt.ylim(0, 100)
plt.legend(title="Broad Genre")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()