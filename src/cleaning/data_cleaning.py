# PAN Cleaning Datasets

import pandas as pd

dig_songs_df = pd.read_csv('../dig_songs_df.csv', parse_dates=['Date'])
hot100_df = pd.read_csv('../hot100_df.csv', parse_dates=['Date'])
radio_df = pd.read_csv('../radio_df.csv', parse_dates=['Date'])
streaming_df = pd.read_csv('../streaming_df.csv', parse_dates=['Date'])



# Dropping null values.
dig_songs_df = dig_songs_df.dropna(subset=['Artist'])
hot100_df = hot100_df.dropna(subset=['Artist'])
radio_df = radio_df.dropna(subset=['Artist'])
streaming_df = streaming_df.dropna(subset=['Artist'])

# Filtering by dates higher than 2020 (included)
dig_songs_df = dig_songs_df.loc[dig_songs_df['Date'] >= '2020-01-01'].copy()
hot100_df = hot100_df.loc[hot100_df['Date'] >= '2020-01-01'].copy()
radio_df = radio_df.loc[radio_df['Date'] >= '2020-01-01'].copy()
streaming_df = streaming_df.loc[streaming_df['Date'] >= '2020-01-01'].copy()



# creating new columns
char = 'Digital'
dig_songs_df.rename(
    columns={'Rank':f'{char} Rank',
             'Last Week':f'{char} Last Week',
             'Peak Position':f'{char} Peak Position',
             'Weeks in Charts':f'{char} Weeks in Charts'
             }
             ,inplace=True
             )

new_columns = ['Date','Year','Month','Song','Artist',f'{char} Rank',f'{char} Last Week',f'{char} Peak Position',f'{char} Weeks in Charts']

dig_songs_df['Year'] = dig_songs_df['Date'].dt.year
dig_songs_df['Month'] = dig_songs_df['Date'].dt.month
dig_songs_df = dig_songs_df[new_columns]


char = 'Hot100'
hot100_df.rename(
    columns={'Rank':f'{char} Rank',
             'Last Week':f'{char} Last Week',
             'Peak Position':f'{char} Peak Position',
             'Weeks in Charts':f'{char} Weeks in Charts'
             }
             ,inplace=True
             )

new_columns = ['Date','Year','Month','Song','Artist',f'{char} Rank',f'{char} Last Week',f'{char} Peak Position',f'{char} Weeks in Charts']

hot100_df['Year'] = hot100_df['Date'].dt.year
hot100_df['Month'] = hot100_df['Date'].dt.month
hot100_df = hot100_df[new_columns]

char = 'Radio'
radio_df.rename(
    columns={'Rank':f'{char} Rank',
             'Last Week':f'{char} Last Week',
             'Peak Position':f'{char} Peak Position',
             'Weeks in Charts':f'{char} Weeks in Charts'
             }
             ,inplace=True
             )

new_columns = ['Date','Year','Month','Song','Artist',f'{char} Rank',f'{char} Last Week',f'{char} Peak Position',f'{char} Weeks in Charts']

radio_df['Year'] = radio_df['Date'].dt.year
radio_df['Month'] = radio_df['Date'].dt.month
radio_df = radio_df[new_columns]

char = 'Streaming'
streaming_df.rename(
    columns={'Rank':f'{char} Rank',
             'Last Week':f'{char} Last Week',
             'Peak Position':f'{char} Peak Position',
             'Weeks in Charts':f'{char} Weeks in Charts'
             }
             ,inplace=True
             )

new_columns = ['Date','Year','Month','Song','Artist',f'{char} Rank',f'{char} Last Week',f'{char} Peak Position',f'{char} Weeks in Charts']

streaming_df['Year'] = streaming_df['Date'].dt.year
streaming_df['Month'] = streaming_df['Date'].dt.month
streaming_df = streaming_df[new_columns]



# Removing non-ASCII characters from the 'Artist' and 'Song' columns in datasets
dig_songs_df['Artist'] = dig_songs_df['Artist'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))
dig_songs_df['Song'] = dig_songs_df['Song'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))

hot100_df['Artist'] = hot100_df['Artist'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))
hot100_df['Song'] = hot100_df['Song'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))

radio_df['Artist'] = radio_df['Artist'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))
radio_df['Song'] = radio_df['Song'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))

streaming_df['Artist'] = streaming_df['Artist'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))
streaming_df['Song'] = streaming_df['Song'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))
