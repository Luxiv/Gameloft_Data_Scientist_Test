"""
2.2 Create a function to count the number of identical characters in a string, returning
the value of the highest count and the letter
"""

import unittest


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

    char_dict = {}
    for symbol in string:
        if symbol not in char_dict:
            char_dict[symbol] = string.count(symbol)

    max_count_letter = max(char_dict, key=lambda key: char_dict[key])
    return char_dict[max_count_letter], max_count_letter


class IdentCharCounterTestCase(unittest.TestCase):
    def test_ident_char_counter_valid_string(self):
        string = "hello"
        expected_result = (2, 'l')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_valid_string_with_repeated_characters(self):
        string = "Mississippi"
        expected_result = (4, 's')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_valid_string_with_same_characters(self):
        string = "aabbbccc"
        expected_result = (3, 'b')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_empty_string(self):
        string = ""
        expected_result = (0, None)

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_invalid_input(self):
        invalid_input = 12345

        with self.assertRaises(TypeError):
            ident_char_counter(invalid_input)


class IdentCharCounterWithCollectionFuncTestCase(unittest.TestCase):
    def test_ident_char_counter_with_collection_func_valid_string(self):
        string = "hello"
        expected_result = (2, 'l')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_with_collection_func_valid_string_with_repeated_characters(self):
        string = "Mississippi"
        expected_result = (4, 's')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_with_collection_func_valid_string_with_same_characters(self):
        string = "aabbbccc"
        expected_result = (3, 'b')

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_with_collection_func_empty_string(self):
        string = ""
        expected_result = (0, None)

        result = ident_char_counter(string)
        self.assertEqual(result, expected_result)

    def test_ident_char_counter_with_collection_func_invalid_input(self):
        invalid_input = 12345

        with self.assertRaises(TypeError):
            ident_char_counter(invalid_input)


if __name__ == '__main__':
    unittest.main()
