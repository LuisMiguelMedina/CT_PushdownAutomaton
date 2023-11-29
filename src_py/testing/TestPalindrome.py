import unittest
from pda.palindrome import PalindromePDA

class Token:
    def __init__(self, t_type):
        self.type = t_type

class TestPalindromePDA(unittest.TestCase):
    def setUp(self):
        self.pda = PalindromePDA()

    def test_empty_string(self):
        self.assertTrue(self.pda.process_tokens([]))

    def test_even_palindromes(self):
        palindromes = ['AA', 'AAAA', 'AAAAAA', 'AABBAA', 'ABAABA', 'ABBA', 'ABBBBA', 'BAAAAB', 'BAAB', 'BABBAB', 'BB', 'BBAABB', 'BBBB', 'BBBBBB']
        for string in palindromes:
            tokens = [Token(char) for char in string]  # Crear tokens como objetos
            self.assertTrue(self.pda.process_tokens(tokens), f"Failed on string: {string}")

    def test_non_palindromes(self):
        non_palindromes = ['A', 'AAA', 'AAAB', 'ABAB', 'BABA']
        for string in non_palindromes:
            tokens = [Token(char) for char in string]  # Crear tokens como objetos
            self.assertFalse(self.pda.process_tokens(tokens), f"Failed on string: {string}")


if __name__ == "__main__":
    unittest.main()
