import pandas as pd

def get_weeks_in_charts_max(artist_list, chart, df):
    """
    Analyzes a DataFrame `df` containing musical chart data to find the maximum number of weeks
    an artist's song spent on the charts.

    Args:
        artist_list (list): A list of artist names to focus on.
        chart: The name of the chart to consider (e.g., "Hot 100", "Billboard 200").
        df (pandas.DataFrame): A DataFrame containing song chart data with columns like
            'Artist', 'Song', 'Year', 'Month', and 'Weeks in Charts'.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'Artist', 'Song', 'Year', 'Month', and
            'Total Weeks in Charts', showing the maximum number of weeks each song by the specified
            artists spent on the charts.
    """
    # Initialize an empty list to store results
    result_list = []

    # Iterate over each artist in the provided list
    for artist in artist_list:
        # Extract unique songs associated with the current artist
        unique_songs_for_artist = df.loc[df['Artist'] == artist, 'Song'].unique()

        # Iterate over each unique song for the current artist
        for song in unique_songs_for_artist:
            # Filter the DataFrame for the current artist and song combination
            filtered_df = df.loc[
                (df['Artist'] == artist) &
                (df['Song'] == song)
            ]

            # Calculate the maximum number of weeks in charts for the current artist and song
            weeks_in_charts_max = filtered_df[f'{chart} Weeks in Charts'].max()

            # Get the 'Year' and 'Month' values for the row with the maximum weeks
            max_weeks_row = filtered_df.loc[filtered_df[f'{chart} Weeks in Charts'] == weeks_in_charts_max].iloc[0]
            year = max_weeks_row['Year']
            month = max_weeks_row['Month']

            # Append the result as a dictionary to the result_list
            result_list.append({
                'Year': year,
                'Month': month,
                'Artist': artist,
                'Song': song,
                f'{chart} Total Weeks in Charts': weeks_in_charts_max
            })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_list)

    # Return the final DataFrame containing the total weeks in charts for each artist and song combination
    return result_df


def get_peak_positions_freq(artist_list, chart, df):
    """
    This function takes a list of artists, a chart name, and a DataFrame containing song data as input,
    and returns a DataFrame showing the peak chart positions and corresponding frequencies for each artist and song.

    Args:
    artist_list: A list of artist names.
    chart: The name of the chart to consider (e.g., "Hot 100", "Billboard 200").
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", "Year", "Month", and the specified chart's peak position.

    Returns:
    A Pandas DataFrame with columns for "Artist", "Song", "Year", "Month", "Peak Position" (for the specified chart), and "Frequency" (number of times the peak position was achieved).
    """
    # Initialize an empty list to store results
    result_list = []

    # Iterate over each artist in the provided list
    for artist in artist_list:
        # Extract unique songs associated with the current artist
        unique_songs_for_artist = df.loc[df['Artist'] == artist, 'Song'].unique()

        # Iterate over each unique song for the current artist
        for song in unique_songs_for_artist:
            # Filter the DataFrame for the current artist and song combination
            filtered_df = df.loc[
                (df['Artist'] == artist) &
                (df['Song'] == song)
            ]

            # Calculate the maximum peak position and frequency for the current artist and song
            max_peak_position = filtered_df[f'{chart} Peak Position'].min()
            frequency = len(filtered_df[filtered_df[f'{chart} Peak Position'] == max_peak_position])

            # Get the 'Year' and 'Month' values for the row with the maximum peak position
            max_peak_position_row = filtered_df.loc[filtered_df[f'{chart} Peak Position'] == max_peak_position].iloc[0]
            year = max_peak_position_row['Year']
            month = max_peak_position_row['Month']

            # Append the result as a dictionary to the result_list
            result_list.append({
                'Year': year,
                'Month': month,
                'Artist': artist, 
                'Song': song, 
                f'{chart} Peak Position': max_peak_position,
                'Frequency': frequency
                })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_list)

    # Return the final DataFrame containing the peak positions for each artist and song combination
    return result_df


def get_best_rank(artist_list, chart, df):
    """
    This function takes a list of artists, a chart name, and a DataFrame containing song data as input,
    and returns a DataFrame showing the best (lowest) chart positions achieved by each artist and song.

    Args:
    artist_list: A list of artist names.
    chart: The name of the chart to consider (e.g., "Hot 100", "Billboard 200").
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", "Year", "Month", and the specified chart's peak position.

    Returns:
    A Pandas DataFrame with columns for "Artist", "Song", "Year", "Month", "Peak Position" (for the specified chart), and "Frequency" (number of times the peak position was achieved).
    """
    # Initialize an empty list to store results
    result_list = []

    # Iterate over each artist in the provided list
    for artist in artist_list:
        # Extract unique songs associated with the current artist
        unique_songs_for_artist = df.loc[df['Artist'] == artist, 'Song'].unique()

        # Iterate over each unique song for the current artist
        for song in unique_songs_for_artist:
            # Filter the DataFrame for the current artist and song combination
            filtered_df = df.loc[
                (df['Artist'] == artist) &
                (df['Song'] == song)
            ]

            # Calculate the best rank for the current artist and song
            best_rank = filtered_df[f'{chart} Peak Position'].min()

            # Get the 'Year' and 'Month' values for the row with the maximum peak position
            max_peak_position_row = filtered_df.loc[filtered_df[f'{chart} Peak Position'] == best_rank].iloc[0]
            year = max_peak_position_row['Year']
            month = max_peak_position_row['Month']

            # Append the result as a dictionary to the result_list
            result_list.append({
                'Year': year,
                'Month': month,
                'Artist': artist, 
                'Song': song, 
                f'{chart} Peak Position': best_rank
                })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_list)

    # Return the final DataFrame containing the best rank for each artist and song combination
    return result_df


def get_total_num_songs(artist_list, chart, df):
    """
    This function calculates the total number of unique songs each artist has released that charted on the Billboard 200 between 2020 and the current date.

    Args:
    artist_list: A list of artist names.
    chart: The chart name to consider.
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", "Year", "Month", and "Bil200 Peak Position".

    Returns:
    A Pandas DataFrame with columns for "Artist", "Year", "Month", and "Bil200 Total Songs in Charts", indicating the number of unique songs each artist has released that charted on the Billboard 200 between 2020 and the current date.
    """
    # Initialize an empty list to store results
    result_list = []

    # Iterate over each artist in the provided list
    for artist in artist_list:
        # Filters the DataFrame for songs by the current artist that charted on the Billboard 200 between 2020 and now.
        filtered_df = df[
            (df['Artist'] == artist) &
            (df[f'{chart} Peak Position'].notna()) &  # Include only songs with a recorded peak position
            (df['Year'].astype(int) >= 2020)  # Filter songs released in 2020 or later
        ]
    
        # Counts the number of unique songs for the current artist in the filtered DataFrame.
        unique_songs_for_artist = filtered_df['Song'].nunique()

        # Get the 'Year' and 'Month' values for the first row (assuming they are consistent for a given artist)
        if not filtered_df.empty:
            year = filtered_df['Year'].iloc[0]
            month = filtered_df['Month'].iloc[0]
        else:
            year = None
            month = None

        # Append the result as a dictionary to the result_list
        result_list.append({
            'Year': year,
            'Month': month,
            'Artist': artist, 
            f'{chart} Total Songs in Charts': unique_songs_for_artist
            })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_list)

    # Return the final DataFrame containing the total num songs for each artist
    return result_df


def create_artist_popularity_df(artist_name, popularity_metrics_flip, target_columns=['Popularity Index Scaled']):
    """
    Creates a DataFrame containing popularity metrics for a specific artist,
    handling missing data by filling in with averages from previous weeks.

    Args:
        artist_name (str): Name of the artist to extract data for.
        popularity_metrics_flip (pandas.DataFrame): DataFrame containing
        popularity metrics with list of columns.

    Returns:
        pandas.DataFrame: DataFrame containing popularity metrics for the
        specified artist, handling missing data with averages.
    """
    # Sort the DataFrame by 'Date'
    popularity_metrics_flip = popularity_metrics_flip.sort_values(by='Date')

    # Iterate over unique dates
    unique_dates = popularity_metrics_flip['Date'].unique()

    new_rows = []  # Store new rows in a list

    # Decay factor parameters
    initial_decay_factor = 0.995  # Initial decay factor
    decay_rate = 0.0017  # Decay rate, adjust as needed

    for i, date in enumerate(unique_dates):
        # Filter rows for the current date and artist
        rows_for_date_artist = popularity_metrics_flip[(popularity_metrics_flip['Date'] == date) & (popularity_metrics_flip['Artist'] == artist_name)]

        # Check if the artist is not present for that date
        if rows_for_date_artist.empty:
            # Calculate the average of the previous 8 weeks for each target column
            previous_8_weeks = popularity_metrics_flip[(popularity_metrics_flip['Date'] < date) & (popularity_metrics_flip['Artist'] == artist_name)].tail(8)
            avg_scores = previous_8_weeks[target_columns].mean()

            # Apply the polynomial decay to the average scores
            decay_factor = initial_decay_factor / (1 + decay_rate * i)
            avg_scores_decay = avg_scores * decay_factor

            # Append the new row to the list
            new_row = {'Date': date, 'Artist': artist_name}
            new_row.update(avg_scores_decay.to_dict())  # Update the dictionary with decayed averages for all columns
            new_rows.append(new_row)

    # Concatenate the new rows to the original DataFrame
    popularity_metrics_flip = pd.concat([popularity_metrics_flip, pd.DataFrame(new_rows)], ignore_index=True)

    # Sort the DataFrame again by 'Date'
    popularity_metrics_flip = popularity_metrics_flip.sort_values(by='Date')

    # Filter the DataFrame for the specified artist
    popularity_artist = popularity_metrics_flip[popularity_metrics_flip['Artist'] == artist_name]

    return popularity_artist





####################################################################################################

##### THIS IN CASE SOMETHING FAILS ######

def create_artist_popularity_df2(artist_name, popularity_metrics_flip):
    """
    Creates a DataFrame containing popularity metrics for a specific artist,
    handling missing data by filling in with averages from previous weeks.

    Args:
        artist_name (str): Name of the artist to extract data for.
        popularity_metrics_flip (pandas.DataFrame): DataFrame containing
        popularity metrics with columns 'Date' and 'Popularity Index Scaled'.

    Returns:
        pandas.DataFrame: DataFrame containing popularity metrics for the
        specified artist, handling missing data with averages.
    """
    # Convert 'Date' column to datetime if needed
    popularity_metrics_flip['Date'] = pd.to_datetime(popularity_metrics_flip['Date'])

    # Iterate over unique dates
    unique_dates = popularity_metrics_flip['Date'].unique()

    new_rows = []  # Store new rows in a list

    for date in unique_dates:
        # Filter rows for the current date and artist
        rows_for_date_artist = popularity_metrics_flip[(popularity_metrics_flip['Date'] == date) & (popularity_metrics_flip['Artist'] == artist_name)]

        # Check if the artist is not present for that date
        if rows_for_date_artist.empty:
            # Calculate the average of the previous 8 weeks
            previous_8_weeks = popularity_metrics_flip[(popularity_metrics_flip['Date'] < date) & (popularity_metrics_flip['Date'] >= date - pd.DateOffset(weeks=8))]
            avg_score = previous_8_weeks['Popularity Index Scaled'].mean()

            # Append the new row to the list
            new_rows.append({'Date': date, 'Artist': artist_name, 'Popularity Index Scaled': avg_score})

    # Concatenate the new rows to the original DataFrame
    popularity_metrics_flip = pd.concat([popularity_metrics_flip, pd.DataFrame(new_rows)], ignore_index=True)

    # Sort the DataFrame again by 'Date'
    popularity_metrics_flip = popularity_metrics_flip.sort_values(by='Date')

    # Filter the DataFrame for the specified artist
    popularity_artist = popularity_metrics_flip[popularity_metrics_flip['Artist'] == artist_name]

    return popularity_artist