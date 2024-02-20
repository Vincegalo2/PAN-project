import pandas as pd
from pytrends.request import TrendReq
import time

def get_google_trends(df,timeframe='2023-01-01 2024-01-01', max_columns=20, row_range=(0, 20)):
    """
    Retrieves search trend data for a list of keywords from a specified dataframe within a specified row range.

    Args:
        df (pandas.DataFrame): The dataframe containing the keyword list.
        timeframe (str, optional): The timeframe for which to retrieve search trend data. Defaults to '2023-01-01 2024-01-01'.
        max_columns (int, optional): The maximum number of columns to allow in the final dataframe. Defaults to 20.
        row_range (tuple, optional): The inclusive range of rows to process from the dataframe. Defaults to (0, 20).

    Returns:
        pandas.DataFrame: A combined dataframe containing the search trend data for the specified keywords.
    """

    # Try-except block to handle any exceptions during data retrieval
    try:
        # Initialize variables
        keyword_dict = {}  # Dictionary to store keywords
        count = 0  # Counter for tracking keyword processing
        df_list = []  # List to store retrieved dataframes

        # Iterate over specified rows in the dataframe
        for index, row in df.iloc[row_range[0]:row_range[1]].iterrows():
            keyword = row['Artist']  # Extract keyword from current row
            keyword_dict[keyword] = keyword  # Add keyword to dictionary
            count += 1

            # Process 5 keywords at a time
            if count == 5:
                # Build payload for Google Trends API call
                pytrend = TrendReq(hl='en-US', tz=360)
                pytrend.build_payload(kw_list=keyword_dict.values(), timeframe=timeframe)

                # Retrieve search trend data from API
                df_temp = pytrend.interest_over_time().drop(columns='isPartial').sort_index(ascending=False)

                # Append retrieved dataframe to list
                df_list.append(df_temp)

                # Check for maximum column limit
                if len(pd.concat(df_list, axis=1).columns) >= max_columns:
                    break

                # Reset counters and clear dictionary for next batch
                count = 0
                keyword_dict.clear()

                # Introduce a delay between requests to avoid rate limiting
                time.sleep(2)  # You can adjust the number of seconds based on the API rate limit

        # Concatenate all retrieved dataframes into a single dataframe
        final_df = pd.concat(df_list, axis=1)

        # Return the final dataframe containing search trend data
        return final_df

    # Handle exceptions during data retrieval
    except Exception as e:
        print('Error retrieving google data:', e)
        return None
