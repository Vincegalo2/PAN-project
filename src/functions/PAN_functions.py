import pandas as pd

def get_weeks_in_charts_max(artist_list, chart, df):
    """
    Analyzes a DataFrame `df` containing musical chart data to find the maximum number of weeks
    an artist's song spent on the charts.

    Args:
        artist_list (list): A list of artist names to focus on.
        chart: The name of the chart to consider (e.g., "Hot 100", "Billboard 200").
        df (pandas.DataFrame): A DataFrame containing song chart data with columns like
            'Artist', 'Song', and 'Weeks in Charts'.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'Artist', 'Song', and 'Total Weeks in Charts',
            showing the maximum number of weeks each song by the specified artists spent on the charts.
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

            # Append the result as a dictionary to the result_list
            result_list.append({
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
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", and the specified chart's peak position.

    Returns:
    A Pandas DataFrame with columns for "Artist", "Song", "Peak Position" (for the specified chart), and "Frequency" (number of times the peak position was achieved).
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

            # Append the result as a dictionary to the result_list
            result_list.append({
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
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", and the specified chart's peak position.

    Returns:
    A Pandas DataFrame with columns for "Artist", "Song", and "Peak Position" (for the specified chart), showing the best (lowest) rank achieved by each artist and song.
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

            # Append the result as a dictionary to the result_list
            result_list.append({
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
    chart: The chart name to consider (in this case, "Bil200").
    df: A Pandas DataFrame containing song data, including columns for "Artist", "Song", and "Bil200 Peak Position".

    Returns:
    A Pandas DataFrame with columns for "Artist" and "Bil200 Total Songs in Charts", indicating the number of unique songs each artist has released that charted on the Billboard 200 between 2020 and the current date.
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

        # Append the result as a dictionary to the result_list
        result_list.append({
            'Artist': artist, 
            f'{chart} Total Songs in Charts': unique_songs_for_artist
            })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_list)

    # Return the final DataFrame containing the total num songs for each artist
    return result_df