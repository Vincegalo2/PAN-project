import pandas as pd

pop_metrics_flip = pd.read_csv('../popularity_metrics_flip.csv')
pop_big_data = pd.read_csv('../popularity_big_data.csv')

df_no_duplicates = pop_metrics_flip.sort_values(by='Popularity Index Scaled', ascending=False).drop_duplicates(['Date', 'Artist'], keep='first')

# Join two dataframes
merged_df = pop_big_data.merge(df_no_duplicates, how='inner', left_index=True, right_index=True)

# Rename some columns
merged_df.rename(columns={'Date_x':'Date','Artist_x':'Artist'}, inplace=True)

# Dropping some columns
merged_df.drop(columns=['Year','Month','Song','Date_y', 'Artist_y', 'Rank Mean Flip','Peak Pos Mean Flip', 'Total Wks in Charts Mean'],inplace=True)

merged_df.to_csv('PAN_index_final.csv',index=False)