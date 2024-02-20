import pandas as pd

digital_ft_df = pd.read_csv('../digital_featured_df.csv')
hot100_ft_df = pd.read_csv('../hot100_featured_df.csv')
radio_ft_df = pd.read_csv('../radio_featured_df.csv')
streaming_ft_df = pd.read_csv('../streaming_featured_df.csv')

# Merging Datasets
tempdf = hot100_ft_df.merge(digital_ft_df
                            ,how='left'
                            ,on=['Artist','Song']
                            )

tempdf['Artist'] = tempdf['Artist'].str.replace('|', ' &')

# Replace missing values with 0
tempdf = tempdf.fillna(
    {'Digital Wks in Charts': 0, 
     'Digital Peak Pos': 0, 
     'Digital Freq in Peak Pos': 0, 
     'Digital Total Num in Charts': 0}
     ).astype({'Digital Wks in Charts': 'int64',
                                 'Digital Peak Pos': 'int64',
                                 'Digital Freq in Peak Pos': 'int64', 
                                 'Digital Total Num in Charts': 'int64'})

tempdf2 = tempdf.merge(radio_ft_df
                        ,how='left'
                        ,on=['Artist','Song']
                        )

tempdf2['Artist'] = tempdf2['Artist'].str.replace('|', ' &')

# Replace missing values with 0
tempdf2 = tempdf2.fillna(
    {'Radio Wks in Charts': 0, 
     'Radio Peak Pos': 0, 
     'Radio Freq in Peak Pos': 0, 
     'Radio Total Num in Charts': 0}
     ).astype({'Radio Wks in Charts': 'int64',
                                 'Radio Peak Pos': 'int64',
                                 'Radio Freq in Peak Pos': 'int64', 
                                 'Radio Total Num in Charts': 'int64'})

tempdf3 = tempdf2.merge(streaming_ft_df
                        ,how='left'
                        ,on=['Artist','Song']
                        )

tempdf3['Artist'] = tempdf3['Artist'].str.replace('|', ' &')

# Replace missing values with 0
tempdf3 = tempdf3.fillna(
    {'Streaming Wks in Charts': 0, 
     'Streaming Peak Pos': 0, 
     'Streaming Freq in Peak Pos': 0, 
     'Streaming Total Num in Charts': 0}
     ).astype({'Streaming Wks in Charts': 'int64',
                                 'Streaming Peak Pos': 'int64',
                                 'Streaming Freq in Peak Pos': 'int64', 
                                 'Streaming Total Num in Charts': 'int64'})


new_column_order = ['Artist', 'Song', 'Hot100 Wks in Charts', 'Digital Wks in Charts', 'Radio Wks in Charts', 'Streaming Wks in Charts', 
                    'Hot100 Peak Pos','Digital Peak Pos', 'Radio Peak Pos', 'Streaming Peak Pos', 
                    'Hot100 Freq in Peak Pos', 'Digital Freq in Peak Pos', 'Radio Freq in Peak Pos', 'Streaming Freq in Peak Pos',
                    'Hot100 Total Num in Charts', 'Digital Total Num in Charts', 'Radio Total Num in Charts', 'Streaming Total Num in Charts'
                    ]  

tempdf3 = tempdf3[new_column_order].copy()
tempdf3.to_csv('popularity_no_dtime_df.csv', index=False)