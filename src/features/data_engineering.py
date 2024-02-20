import pandas as pd
import os
import sys

project_path = '../_PAN_Project'
data_path = os.path.join(project_path, 'src', 'functions')
sys.path.append(data_path)

from PAN_functions import get_weeks_in_charts_max
from PAN_functions import get_peak_positions_freq
from PAN_functions import get_best_rank
from PAN_functions import get_total_num_songs



#################### Datasets from Billboard ##########################

dgt_songs_df = pd.read_csv('../dig_songs_cl_df.csv', parse_dates=['Date'])
hot100_df = pd.read_csv('../hot100_cl_df.csv', parse_dates=['Date'])
radio_df = pd.read_csv('../radio_cl_df.csv', parse_dates=['Date'])
streaming_df = pd.read_csv('../streaming_cl_df.csv', parse_dates=['Date'])


#################### Digital Songs ##########################

dgt_songs_df = dgt_songs_df.drop(columns='Digital Last Week')

# list of all unique artist's names
dgt_songs_list = dgt_songs_df['Artist'].unique()

# Params for the functions
artist_list = dgt_songs_list
df = dgt_songs_df
chart = 'Digital'

# function get_week_in_charts_max
digital_songs_weeks_charts = get_weeks_in_charts_max(artist_list,chart, df)
digital_songs_weeks_charts = digital_songs_weeks_charts.loc[
                            digital_songs_weeks_charts[f'{chart} Total Weeks in Charts'] >= 0
                            ].sort_values(by=f'{chart} Total Weeks in Charts', ascending=False)
# Setting a new index
digital_songs_weeks_charts_df = digital_songs_weeks_charts.reset_index(drop=True)


# function get_peak_positions_freq
digital_peak_positions = get_peak_positions_freq(artist_list, chart, df)
# function get_best_rank
digital_best_rank = get_best_rank(artist_list, chart, df)
# function get_get_total_num_songs
digital_total_num_songs_df = get_total_num_songs(artist_list, chart, df)


# Merging all dataframes into one
dgt_songs_merged_df = digital_songs_weeks_charts.merge(
                    digital_peak_positions
                    ,how='right'
                    ,on=['Song','Artist']
                    ).merge(
                        digital_total_num_songs_df
                        ,how='left'
                        ,on='Artist'
                    )

# Changing feature names
new_columns_list = {'Artist':'Artist'
                    ,'Song':'Song'
                    ,'Digital Total Weeks in Charts':'Digital Wks in Charts'
                    ,'Digital Peak Position':'Digital Peak Pos'
                    ,'Frequency':'Digital Freq in Peak Pos'
                    ,'Digital Total Songs in Charts':'Digital Total Num in Charts'
                    }

dgt_songs_merged_df.rename(columns=new_columns_list, inplace=True)



#################### Hot 100 ##########################

# Removing Unwanted Features
hot100_df = hot100_df.drop(columns='Hot100 Last Week')

# List of all unique artist's names
hot100_list = hot100_df['Artist'].unique()

# Params for the function
artist_list = hot100_list
df = hot100_df
chart = 'Hot100'

# function get_week_in_charts_max
hot100_weeks_charts = get_weeks_in_charts_max(artist_list,chart, df)
hot100_weeks_charts = hot100_weeks_charts.loc[
                            hot100_weeks_charts[f'{chart} Total Weeks in Charts'] >= 0
                            ].sort_values(by=f'{chart} Total Weeks in Charts', ascending=False)

# Setting a new index
hot100_weeks_charts_df = hot100_weeks_charts.reset_index(drop=True)

# function get_peak_positions_freq
hot100_positions = get_peak_positions_freq(artist_list, chart, df)
# function get_best_rank
hot100_best_rank = get_best_rank(artist_list, chart, df)
# function get_total_num_songs
hot100_num_songs_df = get_total_num_songs(artist_list, chart, df)

# Merging all dataframes
hot100_merged_df = hot100_weeks_charts.merge(
                    hot100_positions
                    ,how='right'
                    ,on=['Song','Artist']
                    ).merge(
                        hot100_num_songs_df
                        ,how='left'
                        ,on='Artist'
                    )

new_columns_list = {'Artist':'Artist'
                    ,'Song':'Song'
                    ,'Hot100 Total Weeks in Charts':'Hot100 Wks in Charts'
                    ,'Hot100 Peak Position':'Hot100 Peak Pos'
                    ,'Frequency':'Hot100 Freq in Peak Pos'
                    ,'Hot100 Total Songs in Charts':'Hot100 Total Num in Charts'
                    }

hot100_merged_df.rename(columns=new_columns_list, inplace=True)



#################### Radio ##########################

radio_df = radio_df.drop(columns='Radio Last Week')

# List of all unique artist's names
radio_list = radio_df['Artist'].unique()

# Params for the function
artist_list = radio_list
df = radio_df
chart = 'Radio'

# function get_week_in_charts_max
radio_weeks_charts = get_weeks_in_charts_max(artist_list,chart, df)
radio_weeks_charts = radio_weeks_charts.loc[
                            radio_weeks_charts[f'{chart} Total Weeks in Charts'] >= 0
                            ].sort_values(by=f'{chart} Total Weeks in Charts', ascending=False)

# Setting a new index
radio_weeks_charts_df = radio_weeks_charts.reset_index(drop=True)

# function get_peak_positions_freq
radio_peak_positions = get_peak_positions_freq(artist_list, chart, df)
# function get_total_num_songs
radio_total_num_songs_df = get_total_num_songs(artist_list, chart, df)

radio_total_num_songs_df.sort_values(by='Radio Total Songs in Charts',ascending=False).reset_index(drop=True)

# Merging all dataframes
radio_merged_df = radio_weeks_charts_df.merge(
                    radio_peak_positions
                    ,how='right'
                    ,on=['Song','Artist']
                    ).merge(
                        radio_total_num_songs_df
                        ,how='left'
                        ,on='Artist'
                    )

new_columns_list = {'Artist':'Artist'
                    ,'Song':'Song'
                    ,'Radio Total Weeks in Charts':'Radio Wks in Charts'
                    ,'Radio Peak Position':'Radio Peak Pos'
                    ,'Frequency':'Radio Freq in Peak Pos'
                    ,'Radio Total Songs in Charts':'Radio Total Num in Charts'
                    }

radio_merged_df.rename(columns=new_columns_list, inplace=True)



#################### Streaming ##########################

streaming_df = streaming_df.drop(columns='Streaming Last Week')

# List of all unique artist's names
streaming_list = streaming_df['Artist'].unique()

# Params for the function
artist_list = streaming_list
df = streaming_df
chart = 'Streaming'

# function get_week_in_charts_max
streaming_weeks_charts = get_weeks_in_charts_max(artist_list,chart, df)
streaming_weeks_charts = streaming_weeks_charts.loc[
                            streaming_weeks_charts[f'{chart} Total Weeks in Charts'] >= 0
                            ].sort_values(by=f'{chart} Total Weeks in Charts', ascending=False)

# Setting a new index
streaming_weeks_charts_df = streaming_weeks_charts.reset_index(drop=True)

# function get_peak_positions_freq
streaming_peak_positions = get_peak_positions_freq(artist_list, chart, df)
# function get_total_num_songs
streaming_total_num_songs_df = get_total_num_songs(artist_list, chart, df)

streaming_merged_df = streaming_weeks_charts_df.merge(
                    streaming_peak_positions
                    ,how='right'
                    ,on=['Song','Artist']
                    ).merge(
                        streaming_total_num_songs_df
                        ,how='left'
                        ,on='Artist'
                    )

new_columns_list = {'Artist':'Artist'
                    ,'Song':'Song'
                    ,'Streaming Total Weeks in Charts':'Streaming Wks in Charts'
                    ,'Streaming Peak Position':'Streaming Peak Pos'
                    ,'Frequency':'Streaming Freq in Peak Pos'
                    ,'Streaming Total Songs in Charts':'Streaming Total Num in Charts'
                    }

streaming_merged_df.rename(columns=new_columns_list, inplace=True)



#################### Uploading ##########################

dgt_songs_merged_df.to_csv('digital_featured_df.csv', index=False)
hot100_merged_df.to_csv('hot100_featured_df', index=False)
radio_merged_df.to_csv('radio_featured_df', index=False)
streaming_merged_df.to_csv('streaming_featured_df', index=False)