"""
3.1 You are given a DataFrame that contains information about which items users have
bought in our games. The DataFrame has the following structure:

    cash     game  item_id  username
0  10.99     asp8       14    125335
1   7.99  minions        3    125335
2  10.99     asp8       14   4334123
3   7.99  minions       14   4334123
4   3.99     asp8        7    125335

Write a method that, taking this DataFrame as an input, calculates the sum of money each
user has spent per game, thus producing the following output:

                      cash
username  game
125335    asp8       14.98
          minions     7.99
4334123   asp8       10.99
          minions     7.99
"""

import pandas as pd

USERNAME_COLUMN = 'username'
GAME_COLUMN = 'game'
CASH_COLUMN = 'cash'


def process_dataframe(df: pd.DataFrame):
    """
    Takes a DataFrame and returns a new DataFrame with grouped and summed cash values.

    Args:
        df (pd.DataFrame): Input DataFrame with columns 'cash', 'game', 'item_id', and 'username'.

    Returns:
        pd.DataFrame: A new DataFrame with the cash values grouped by 'username' and 'game'.
    """

    grouped_df = df.groupby([USERNAME_COLUMN, GAME_COLUMN])[CASH_COLUMN].sum()

    return grouped_df


if __name__ == "__main__":
    data = {
        CASH_COLUMN: [10.99, 7.99, 10.99, 7.99, 3.99],
        GAME_COLUMN: ['asp8', 'minions', 'asp8', 'minions', 'asp8'],
        'item_id': [14, 3, 14, 14, 7],
        USERNAME_COLUMN: [125335, 125335, 4334123, 4334123, 125335]
    }

    df = pd.DataFrame(data)

    result = process_dataframe(df)
    print(result)
