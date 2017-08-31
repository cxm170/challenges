import pandas as pd
import numpy as np

# Encode day to one of 1, 10, 100, 1000, ...
def encodeDay(x):
    result = '1'
    num_of_zero = x - 1
    for zero in range(x-1):
        result += '0'
    return int(result)

# Given a string, find the longest substring with repetitive '1'
def getStreak(x):
    x = str(x)
    streak = 0
    
    tmpStreak = 0
    previousElement = '0'
    for element in x:
        if previousElement == '0':
            if element == '1':
                tmpStreak += 1
                previousElement = '1'
        else:
            if element == '1':
                tmpStreak += 1
            else:
                if tmpStreak > streak:
                    streak = tmpStreak
                previousElement = '0'
                tmpStreak = 0
    if tmpStreak > streak:
        streak = tmpStreak
    return streak


pd.set_option('display.max_columns', None)

df = pd.read_csv('./reddit_posts_2016_09_week_1.csv')

df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s', utc=True).apply(lambda x: x.day)

g = df.groupby(['created_utc', 'author'], as_index=False).subreddit.count()

g['code'] = g['created_utc'].apply(lambda x:encodeDay(x))

result = g.groupby(['author'], as_index=False).code.sum()

result['streak'] = result['code'].apply(lambda x: getStreak(x))

result.sort_values(['streak', 'author'], ascending=[False, True]).to_csv('9gag_2.csv', sep='\t', index=False)