
"""
2.2 Create a function to count the number of identical characters in a string, returning
the value of the highest count and the letter
"""


def ident_char_counter(string: str):
    """
        Counts the number of identical characters in a string and returns the value of the highest count and the letter.

        Args:
            string (str): The input string.

        Returns:
            tuple: A tuple containing the highest count and the corresponding letter.
    """
    if type(string) is str:
        string = string.lower()

        char_dict = {}
        highest_count = 0
        highest_symbol = None

        for symbol in string:
            if symbol in char_dict:
                char_dict[symbol] += 1
            else:
                char_dict[symbol] = 1

            if char_dict[symbol] > highest_count:
                highest_count = char_dict[symbol]
                highest_symbol = symbol
        return highest_count, highest_symbol
    else:
        raise TypeError("Not a string, please pass data with type 'str'")


# Test case 1
string1 = "hello"
result1 = ident_char_counter(string1)
print(result1)  # Output: (2, 'l')

# Test case 2
string2 = "Mississippi"
result2 = ident_char_counter(string2)
print(result2)  # Output: (4, 's')

# Test case 3
string3 = "aabbbccc"
result3 = ident_char_counter(string3)
print(result3)  # Output: (3, 'b')

# Test case 4 (empty string)
string4 = ""
result4 = ident_char_counter(string4)
print(result4)  # Output: (0, None)

# Test case 5 (non-string input)
string5 = 12345
result5 = ident_char_counter(string5)
# Output: TypeError: Not a string, please pass data with type 'str'
