"""
2.2 Create a function to count the number of identical characters in a string, returning
the value of the highest count and the letter
"""

import unittest
from collections import Counter


def ident_char_counter(string: str):
    """
        Counts the number of identical characters in a string and returns the value of the highest count and the letter.

        Args:
            string (str): The input string.

        Returns:
            tuple: A tuple containing the highest count and the corresponding letter.
    """
    if not isinstance(string, str):
        raise TypeError("Not a string, please pass data with type 'str'")

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


def ident_char_counter_with_collection_func(string: str):
    """
    Counts the number of identical characters in a string and returns the value of the highest count and the letter.

    Args:
        string (str): The input string.

    Returns:
        tuple: A tuple containing the highest count and the corresponding letter.
    """
    if not isinstance(string, str):
        raise TypeError("Not a string, please pass data with type 'str'")

    string = string.lower()

    char_counts = Counter(string)
    max_count_letter = max(char_counts, key=char_counts.get)
    return char_counts[max_count_letter], max_count_letter


class IdentCharCounterTestCase(unittest.TestCase):
    def test_ident_char_counter(self):
        test_cases = [
            ("hello", (2, 'l')),
            ("Mississippi", (4, 's')),
            ("aabbbccc", (3, 'b')),
            ("", (0, None)),
            (12345, TypeError),
        ]

        for string, expected_result in test_cases:
            if expected_result == TypeError:
                with self.assertRaises(TypeError):
                    ident_char_counter(string)
            else:
                result = ident_char_counter(string)
                self.assertEqual(result, expected_result)


class IdentCharCounterWithCollectionFuncTestCase(unittest.TestCase):
    def test_ident_char_counter_with_collection_func(self):
        test_cases = [
            ("hello", (2, 'l')),
            ("Mississippi", (4, 's')),
            ("aabbbccc", (3, 'b')),
            ("", (0, None)),
            (12345, TypeError),
        ]

        for string, expected_result in test_cases:
            if expected_result == TypeError:
                with self.assertRaises(TypeError):
                    ident_char_counter(string)
            else:
                result = ident_char_counter(string)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
