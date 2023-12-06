import unittest
from lexer.lexer import begin_lexing
from pda.palindrome import PalindromePDA

class Token:
    def __init__(self, t_type, t_value):
        self.type = t_type
        self.value = t_value

class TestPalindromePDA(unittest.TestCase):

    def process_string(self, string):
        pda = PalindromePDA()
        tokens = begin_lexing(string)
        valid_tokens = [Token(token.type, token.value) for token in tokens if token.type != 'ERROR']
        total_length = len(valid_tokens)

        for index, token in enumerate(valid_tokens):
            pda.process_token(token.value, index, total_length)

        return pda.get_current_state()

    def test_valid_palindromes(self):
        palindromes = ['aa', 'aba', 'aabaa', 'bb', 'bab', 'bbb', 'aaa']
        for string in palindromes:
            current_state = self.process_string(string)
            self.assertEqual(current_state, 'f', f"Failed on valid palindrome: {string}")

    def test_invalid_palindromes(self):
        non_palindromes = ['ab', 'baa', 'abab', 'bba', 'aab']
        for string in non_palindromes:
            current_state = self.process_string(string)
            self.assertNotEqual(current_state, 'f', f"Failed on invalid palindrome: {string}")

    def test_illegal_characters(self):
        illegal_strings = ['ac', 'bd', '1a', 'a1', 'a!']
        for string in illegal_strings:
            tokens = begin_lexing(string)
            self.assertTrue(any(token.type == 'ERROR' for token in tokens), f"Failed on illegal string: {string}")
