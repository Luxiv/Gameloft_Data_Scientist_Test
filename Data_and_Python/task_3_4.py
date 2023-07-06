"""
3.4 You are provided with two DataFrames: User_Time_Info which shows when Users
installed and how long they have played for in minutes, and User_Currency_Info which
shows what their in-game balance was for certain dates the week after install. These are
found below:

        User_Time_Info

    Users Install_Date  Time_Played
0  User_0   2018-06-08           59
1  User_1   2018-06-05           89
2  User_2   2018-06-04           56
3  User_3   2018-06-08           78
4  User_4   2018-06-01           80
5  User_5   2018-06-02           60

        User_Currency_Info

    Users Session_Date  Currency_Balance
0  User_1   2018-06-06               396
1  User_3   2018-06-09               235
2  User_5   2018-06-05               316
3  User_5   2018-06-03               418
4  User_3   2018-06-11               330
5  User_5   2018-06-05               558
6  User_1   2018-06-07               354
7  User_0   2018-06-12               357
8  User_1   2018-06-09               200
9  User_6   2018-06-29               234

Write a function to join the two DataFrames, and then calculate the days from install
between the Session_Date and Install_Date for each entry in the User_Currency_Info
DataFrame. Then reshape the joined DataFrame so we have days since install as
the index, Users as columns, and the values are the Currency_Balance. The answer
should look like the following:

Users              User_0 User_1 User_3 User_5
Days_Since_Install
1                       -  396.0  235.0  418.0
2                       -  354.0      -      -
3                       -      -  330.0  874.0
4                   357.0  200.0      -      -

"""

import pandas as pd


def reshape_data(user_time_info: pd.DataFrame, user_currency_info: pd.DataFrame):
    """
    Join two DataFrames and reshape the data based on days since install.

    Args:
        user_time_info (DataFrame): DataFrame containing user time information.
        user_currency_info (DataFrame): DataFrame containing user currency information.

    Returns:
        DataFrame: Reshaped DataFrame with days since install as the index, users as columns, and currency balance as values.
    """

    user_time_info['Install_Date'] = pd.to_datetime(user_time_info['Install_Date'])
    user_currency_info['Session_Date'] = pd.to_datetime(user_currency_info['Session_Date'])

    joined_df = user_currency_info.merge(user_time_info, on='Users')

    joined_df['Days_Since_Install'] = (joined_df['Session_Date'] - joined_df['Install_Date']).dt.days

    reshaped_df = joined_df.pivot_table(index='Days_Since_Install', columns='Users', values='Currency_Balance',
                                        aggfunc='sum', fill_value='-')

    return reshaped_df


if __name__ == "__main__":

    user_time_info = {
        'Users': ['User_0', 'User_1', 'User_2', 'User_3', 'User_4', 'User_5'],
        'Install_Date': ['2018-06-08', '2018-06-05', '2018-06-04', '2018-06-08', '2018-06-01', '2018-06-02'],
        'Time_Played': [59, 89, 56, 78, 80, 60]
    }

    user_currency_info = {
        'Users': ['User_1', 'User_3', 'User_5', 'User_5', 'User_3', 'User_5', 'User_1', 'User_0', 'User_1', 'User_6'],
        'Session_Date': ['2018-06-06', '2018-06-09', '2018-06-05', '2018-06-03', '2018-06-11', '2018-06-05', '2018-06-07',
                         '2018-06-12', '2018-06-09', '2018-06-29'],
        'Currency_Balance': [396, 235, 316, 418, 330, 558, 354, 357, 200, 234]
    }

    user_time_df = pd.DataFrame(user_time_info)
    user_currency_df = pd.DataFrame(user_currency_info)

    result = reshape_data(user_time_df, user_currency_df)
    print(result)
