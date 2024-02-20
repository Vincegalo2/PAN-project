import pandas as pd
from sklearn.preprocessing import StandardScaler

artist_popularity_df = pd.read_csv('../popularity_no_dtime_df.csv')


# Calculating a weighted formula for Popularity Index
def calculate_weighted_average(row, weights):
    return sum(w * val for w, val in zip(weights, row))

# Columns for which you want to calculate the weighted average
columns_to_average1 = ['Hot100 Wks in Charts', 'Digital Wks in Charts', 'Radio Wks in Charts', 'Streaming Wks in Charts']
columns_to_average2 = ['Hot100 Peak Pos', 'Digital Peak Pos', 'Radio Peak Pos', 'Streaming Peak Pos']
columns_to_average3 = ['Hot100 Freq in Peak Pos', 'Digital Freq in Peak Pos', 'Radio Freq in Peak Pos', 'Streaming Freq in Peak Pos']
columns_to_sum = ['Hot100 Total Num in Charts', 'Digital Total Num in Charts', 'Radio Total Num in Charts', 'Streaming Total Num in Charts']

# Assign weights
weights = [0.5, 0.1, 0.1, 0.3]


for i, row in artist_popularity_df[columns_to_average1].iterrows():
    # Calculate weighted average
    weighted_average = calculate_weighted_average(row, weights)
    
    # Append the result to a new column
    artist_popularity_df.at[i, 'Hot100 Chart mean'] = weighted_average


for i, row in artist_popularity_df[columns_to_average2].iterrows():
    # Calculate weighted average
    weighted_average = calculate_weighted_average(row, weights)
    
    # Append the result to a new column
    artist_popularity_df.at[i, 'Peak Pos mean'] = weighted_average


for i, row in artist_popularity_df[columns_to_average3].iterrows():
    # Calculate weighted average
    weighted_average = calculate_weighted_average(row, weights)
    
    # Append the result to a new column
    artist_popularity_df.at[i, 'Freq in Peak Pos mean'] = weighted_average


for i, row in artist_popularity_df[columns_to_sum].iterrows():
    # Calculate weighted average
    result_sum = row.sum()
    
    # Append the result to a new column
    artist_popularity_df.at[i, 'Total Songs in Charts'] = result_sum


columns_to_popularity = [
    'Hot100 Chart mean',
    'Peak Pos mean',
    'Freq in Peak Pos mean',
    'Total Songs in Charts'
    ]

# Assign weights to each column
weights = [0.35, 0.3, 0.15, 0.2]

for i, row in artist_popularity_df[columns_to_popularity].iterrows():
    # Calculate weighted average
    result_sum = (row * weights).sum()
    
    # Append the result to a new column
    artist_popularity_df.at[i, 'Popularity Index'] = result_sum


columns_to_popularity_index = ['Artist', 'Song','Hot100 Chart mean', 'Peak Pos mean', 'Freq in Peak Pos mean',
       'Total Songs in Charts', 'Popularity Index']
popularity_index_df = artist_popularity_df[columns_to_popularity_index]



# Uploading Dataset
popularity_index_df.to_csv('popularity_index.csv', index=False)