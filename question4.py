import pandas as pd
import matplotlib.pyplot as plt

# Load data
hot_stuff = pd.read_csv('hotstuff.csv')
hot_100 = pd.read_csv('hot100_audio.csv')

hot_stuff['WeekID'] = pd.to_datetime(hot_stuff['WeekID'])

# Merge datasets
df = hot_stuff.merge(hot_100, on='SongID', how='left')

# Fix column names
df.rename(columns={'Performer_x':'Performer'}, inplace=True)
df.drop(columns=['Song_y','Performer_y'], inplace=True)
df.rename(columns={'Song_x':'Song'}, inplace=True)

# Count unique songs per performer
song_counts = df.groupby('Performer')['SongID'].nunique().reset_index()
song_counts.columns = ['Performer', 'NumSongs']
df = df.merge(song_counts, on='Performer', how='left')

# Identify one-hit wonders and superstars
df['OneHitWonder'] = df['NumSongs'] == 1
superstars = df[df['NumSongs'] >= 5]

# Track first charting song for each superstar
superstar_debut_idx = superstars.groupby('Performer')['WeekID'].idxmin()
superstar_debut_songs = df.loc[superstar_debut_idx]

# Average chart positions by weeks on chart
ohw_trajectory = (
    df[df['OneHitWonder']]
    .groupby('Weeks on Chart')['Week Position']
    .mean()
    .reset_index()
)

superstar_trajectory = (
    df[df['SongID'].isin(superstar_debut_songs['SongID'])]
    .groupby('Weeks on Chart')['Week Position']
    .mean()
    .reset_index()
)

# Limit to 55 weeks or less for both groups
max_weeks = 55
ohwt_limited = ohw_trajectory[ohw_trajectory['Weeks on Chart'] <= max_weeks]
superstar_limited = superstar_trajectory[superstar_trajectory['Weeks on Chart'] <= max_weeks]

# Plot
plt.figure(figsize=(12,6))
plt.plot(ohwt_limited['Weeks on Chart'], ohwt_limited['Week Position'], marker='o', label='One-Hit Wonders')
plt.plot(superstar_limited['Weeks on Chart'], superstar_limited['Week Position'], marker='o', label='Superstar Debut Singles (≥ 5 hits)')

plt.gca().invert_yaxis()
plt.xlabel('Weeks on Chart')
plt.ylabel('Average Chart Position')
plt.title('Chart Trajectories: One-Hit Wonders vs Superstars')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
