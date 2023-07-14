import pandas as pd


def calculate_active_days(df: pd.DataFrame):
    """
        Calculates the number of active days per user and the corresponding number of players and their proportion.

        Args:
            df (pandas.DataFrame): Input DataFrame containing 'user_id' and 'event_date' columns.

        Returns:
            pandas.DataFrame: DataFrame with columns 'ActiveDays', 'Number of players', and 'Part of players',
                              sorted by ascending 'ActiveDays'.
        """
    df['event_date'] = pd.to_datetime(df['event_date'])

    active_days_df = df.groupby('user_id')['event_date'].apply(lambda x: x.dt.date.nunique()).reset_index()
    active_days_df.columns = ['user_id', 'ActiveDays']

    total_players = df['user_id'].nunique()

    result_df = active_days_df.groupby('ActiveDays').size().reset_index(name='Number of players')
    result_df['Part of players'] = (result_df['Number of players'] / total_players * 100).round(2).astype(str) + '%'

    return result_df


if __name__ == "__main__":
    # test dataset for Session table
    data_session = {
        'user_id': [1, 1, 2, 2, 3, 3, 4, 5, 6, 6],
        'event_date': ['2023-07-01 10:00:00', '2023-07-01 15:00:00', '2023-07-01 11:30:00', '2023-07-02 14:00:00',
                       '2023-07-03 09:00:00', '2023-07-03 12:30:00', '2023-07-04 16:00:00', '2023-07-05 10:30:00',
                       '2023-07-05 15:45:00', '2023-07-06 11:00:00'],
        'session_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'last_session_length': [500, 600, 800, 700, 900, 550, 400, 750, 550, 650]
    }

    df = pd.DataFrame(data_session)
    res = calculate_active_days(df)

    print(res)
