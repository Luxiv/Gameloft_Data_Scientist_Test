"""
3.3 You are given a DataFrame that contains information about how much users have
spent in a game per day. The DataFrame has the following structure:
     User  Day  Cash
0   user1    1  6.99
1   user1    4  3.99
2   user1    0  7.99
3   user1    5  0.99
4   user2    2  2.99
5   user2    3  8.99
6   user2    4  2.99
7   user2    3  7.99
8   user3    5  1.99
9   user3    2  5.99
10  user3    1  6.99
11  user3    3  5.99

Write a function to manipulate the DataFrame to cumulatively sum how much money
each user has spent. Use this to work out the percentage of the cumulative total the
user has spent per day. The output should look like this:
             Cash  CumSum  Percentage_cs
User  Day
user1 0      7.99   7.99       40.03
      1      6.99   14.98      75.05
      4      3.99   18.97      95.04
      5      0.99   19.96      100.00
user2 2      2.99    2.99      13.02
      3     16.98   19.97      86.98
      4      2.99   22.96      100.00
user3 1      6.99    6.99      33.35
      2      5.99   12.98      61.93
      3      5.99   18.97      90.51
      5      1.99   20.96      100.00
"""

import pandas as pd


def calculate_cumulative_spending(df):
    """
    Calculate the cumulative spending and percentage of total spending for each user.

    Args:
        df (pandas.DataFrame): Input DataFrame with columns 'User', 'Day', and 'Cash'.

    Returns:
        pandas.DataFrame: DataFrame with additional columns 'CumSum' (cumulative spending) and 'Percentage_cs'
            (percentage of total spending).
    """

    # Sort the DataFrame by User and Day
    df.sort_values(by=['User', 'Day'], inplace=True)

    # Calculate the cumulative sum and percentage
    df['CumSum'] = df.groupby('User')['Cash'].cumsum()
    df['Percentage_cs'] = (df['CumSum'] / df.groupby(['User'])['Cash'].transform('sum')) * 100

    # Round the Percentage_cs column to two decimal places
    df['Percentage_cs'] = df['Percentage_cs'].round(2)

    # Set the multi-level index
    df.set_index(['User', 'Day'], inplace=True)

    return df


# Example DataFrame
data = {
    'User': ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3',
             'user3'],
    'Day': [1, 4, 0, 5, 2, 3, 4, 3, 5, 2, 1, 3],
    'Cash': [6.99, 3.99, 7.99, 0.99, 2.99, 8.99, 2.99, 7.99, 1.99, 5.99, 6.99, 5.99]
}

df = pd.DataFrame(data)


# Calling the function and printing the result
res = calculate_cumulative_spending(df)
print(res)
