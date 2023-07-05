
"""
3.2 You are provided with a DataFrame that contains details about users and the cash they
have spent in the last month in in-app purchases. The DataFrame has the following
structure:
    cash    cred_int
0  10.99  1049579531
1   0.00   974308899
2  83.40   123643404
3   0.99  1067477738
4  13.99    12454242
"""

import pandas as pd


def categorize_users(df):
    """
    Categorizes users based on their spending behavior.

    Args:
        df (pd.DataFrame): Input DataFrame with columns 'cash' and 'cred_int'.

    Returns:
        pd.DataFrame: DataFrame containing three categories of users: whales, paying users, and non-paying users.
    """
    # Whales: Users that have spent more than 50 euros
    whales = df[df['cash'] > 50]

    # Paying users: Users that have made purchases but are not whales
    paying_users = df[(df['cash'] > 0) & (df['cash'] <= 50)]

    # Non-paying users: Users that have not made any purchases
    non_paying_users = df[df['cash'] == 0]

    return whales, paying_users, non_paying_users


# Example DataFrame
data = {
    'cash': [10.99, 0.00, 83.40, 0.99, 13.99],
    'cred_int': [1049579531, 974308899, 123643404, 1067477738, 12454242]
}

df = pd.DataFrame(data)

# Categorize the users
whales, paying_users, non_paying_users = categorize_users(df)

# Display the categorized DataFrames
print("Whales:")
print(whales)
print("\nPaying Users:")
print(paying_users)
print("\nNon-Paying Users:")
print(non_paying_users)

