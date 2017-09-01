# Basic idea:
# 1. Get a list with distinct tuples (created_utc, author)
# 2. Convert to created_utc to special code
# 3. Sum up those created_utc codes for each author
# 4. Find the longest consecutive '1's in the sum (converted to String) of each author
# 5. Sort by the streak

import pandas as pd

# Encode day to one of 1, 10, 100, 1000, ...
def encodeDay(x):
    result = '1'
    num_of_zero = x - 1
    for zero in range(x-1):
        result += '0'
    return int(result)

# Given a string, find the longest substring with repetitive '1's
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

df = pd.read_csv('./reddit_posts_2016_09_week_1.csv')

# Convert created_utc to day (1, 2, ..., 31)
df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s', utc=True).apply(lambda x: x.day)

# Get a list with distinct tuples (created_utc, author)
g = df.groupby(['created_utc', 'author'], as_index=False).subreddit.count()

# Convert to created_utc to special code
g['code'] = g['created_utc'].apply(lambda x:encodeDay(x))

# Sum up those created_utc codes for each author
result = g.groupby(['author'], as_index=False).code.sum()

# Find the longest consecutive '1's in the sum (converted to String) of each author
result['streak'] = result['code'].apply(lambda x: getStreak(x))

# Sort by streak, and save to a local file
result.sort_values(['streak', 'author'], ascending=[False, True]).to_csv('9gag_2.csv', sep='\t', index=False)