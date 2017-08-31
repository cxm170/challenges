import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('./reddit_posts_2016_09_week_1.csv')

df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s', utc=True).apply(lambda x: x.date())

df_agg = df.groupby(['created_utc', 'subreddit','author'], as_index=False).title.count().sort_values(['created_utc', 'subreddit', 'title'], ascending=[True, True, False])

df_agg.columns.values[3] = 'count'

df_agg.to_csv('9gag_1.csv', sep='\t', index=False)