import numpy as np 
import pandas as pd

hot100_df = pd.read_csv('../hot100_cl_df.csv', parse_dates=['Date'])
digital_df = pd.read_csv('../dig_songs_cl_df.csv', parse_dates=['Date'])
radio_df = pd.read_csv('../radio_cl_df.csv', parse_dates=['Date'])
streaming_df = pd.read_csv('../streaming_cl_df.csv', parse_dates=['Date'])

hot100_df = hot100_df.drop(columns='Hot100 Last Week')
digital_df = digital_df.drop(columns='Digital Last Week')
radio_df = radio_df.drop(columns='Radio Last Week')
streaming_df = streaming_df.drop(columns='Streaming Last Week')

tempdf = hot100_df.merge(
            digital_df,
            how='left',
            on=['Artist','Song','Date','Year','Month']
        ).merge(
            radio_df,
            how='left',
            on=['Artist','Song','Date','Year','Month']
        ).merge(
            streaming_df,
            how='left',
            on=['Artist','Song','Date','Year','Month']
        )

tempdf['Artist'] = tempdf['Artist'].str.replace('|', ' &')

# Replace missing values with 0
tempdf = tempdf.fillna(
    {'Digital Rank': 0, 
     'Digital Peak Position': 0, 
     'Digital Weeks in Charts': 0,
     'Radio Rank': 0, 
     'Radio Peak Position': 0, 
     'Radio Weeks in Charts': 0,
     'Streaming Rank': 0, 
     'Streaming Peak Position': 0, 
     'Streaming Weeks in Charts': 0}
     ).astype({'Digital Rank': 'int64',
                'Digital Peak Position': 'int64',
                'Digital Weeks in Charts': 'int64',
                'Radio Rank': 'int64',
                'Radio Peak Position': 'int64',
                'Radio Weeks in Charts': 'int64',
                'Streaming Rank': 'int64',
                'Streaming Peak Position': 'int64',
                'Streaming Weeks in Charts': 'int64'})

new_column_order = ['Date', 'Year', 'Month', 'Artist', 'Song', 
                    'Hot100 Rank', 'Digital Rank', 'Radio Rank', 'Streaming Rank',
                    'Hot100 Peak Position', 'Digital Peak Position', 'Radio Peak Position', 'Streaming Peak Position',
                    'Hot100 Weeks in Charts', 'Digital Weeks in Charts', 'Radio Weeks in Charts', 'Streaming Weeks in Charts']

tempdf = tempdf[new_column_order]
popularity_time_index = tempdf

popularity_big_data = popularity_time_index.copy()



###################### Weighted Average Calculations #########################

def calculate_weighted_average1(row, weights):
    return sum(w * val for w, val in zip(weights, row))

def calculate_weighted_average2(row, weights):
    # Identify zero values in the row
    zeros = (row == 0)
    
    # If there are no zeros, calculate the regular weighted average
    if not any(zeros):
        return np.average(row, weights=weights)

    # If there are zeros, calculate the adjusted average excluding zeros
    non_zero_indices = np.where(row != 0)[0]
    non_zero_values = row.iloc[non_zero_indices]
    non_zero_weights = np.array([weights[i] for i in non_zero_indices])

    # Calculate adjusted average
    adjusted_average = np.sum(non_zero_values * non_zero_weights) / np.sum(non_zero_weights)

    return adjusted_average


# Columns for which you want to calculate the weighted average
columns_to_average1 = ['Hot100 Rank','Digital Rank', 'Radio Rank', 'Streaming Rank']
columns_to_average2 = ['Hot100 Peak Position','Digital Peak Position', 'Radio Peak Position','Streaming Peak Position']
columns_to_average3 = ['Hot100 Weeks in Charts', 'Digital Weeks in Charts', 'Radio Weeks in Charts','Streaming Weeks in Charts']

# Assign weights
weights1 = [0.4, 0.1, 0.2, 0.3]
weights2 = [0.4, 0.1, 0.1, 0.4]
weights3 = [0.3, 0.2, 0.2, 0.3]

for i, row in popularity_time_index.iterrows():
    row1 = row[columns_to_average1]
    row2 = row[columns_to_average2]
    row3 = row[columns_to_average3]

    weighted_average1 = calculate_weighted_average2(row1, weights1)
    weighted_average2 = calculate_weighted_average2(row2, weights2)
    weighted_average3 = calculate_weighted_average1(row3, weights3)

    popularity_time_index.at[i, 'Total Rank Mean'] = weighted_average1
    popularity_time_index.at[i, 'Peak Pos in Charts Mean'] = weighted_average2
    popularity_time_index.at[i, 'Total Wks in Charts Mean'] = weighted_average3




###################### Flip Scores ##############################
    
def flip_score(original_score, max_score=100, min_score=1):
    return (max_score + min_score) - original_score

columns_to_flip = ['Total Rank Mean','Peak Pos in Charts Mean']

for i, row in popularity_time_index.iterrows():
    popularity_time_index.at[i, 'Rank Mean Flip'] = flip_score(row['Total Rank Mean'])
    popularity_time_index.at[i, 'Peak Pos Mean Flip'] = flip_score(row['Peak Pos in Charts Mean'])

popularity_metrics_flip = popularity_time_index[['Date', 'Artist','Rank Mean Flip', 'Peak Pos Mean Flip', 'Total Wks in Charts Mean']]




##################### Scaled Index ##############################

columns_to_popularity = ['Rank Mean Flip','Peak Pos Mean Flip','Total Wks in Charts Mean']

# Assign weights to each column
weights = [0.3, 0.4, 0.3]

for i, row in popularity_metrics_flip[columns_to_popularity].iterrows():
    # Calculate weighted average
    result_sum = (row * weights).sum()
    
    # Append the result to a new column
    popularity_metrics_flip.loc[i, 'Popularity Index'] = result_sum

# Scale the 'Popularity Index' to (1 to 100)
min_value = popularity_metrics_flip['Popularity Index'].min()
max_value = popularity_metrics_flip['Popularity Index'].max()

popularity_metrics_flip['Popularity Index Scaled'] = 1 + ((popularity_metrics_flip['Popularity Index'] - min_value) /
                                                         (max_value - min_value)) * 99


# Uploading Dataset
popularity_metrics_flip = popularity_metrics_flip.drop(columns='Popularity Index').copy()
popularity_metrics_flip.to_csv('popularity_metrics_flip.csv',index=False)
popularity_big_data.to_csv('popularity_big_data.csv', index=False)
