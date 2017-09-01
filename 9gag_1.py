import pandas as pd

# Assume the raw data file is stored in the same directory
df = pd.read_csv('./reddit_posts_2016_09_week_1.csv')

# Format the timestamp to date
df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s', utc=True).apply(lambda x: x.date())

# Get the leaderboards for different subreddits in different days
df_agg = df.groupby(['created_utc', 'subreddit','author'], as_index=False).title.count().sort_values(['created_utc', 'subreddit', 'title'], ascending=[True, True, False])

# Rename the 'author' column to 'count'
df_agg.columns.values[3] = 'count'

# Save to a local csv file
df_agg.to_csv('9gag_1.csv', sep='\t', index=False)