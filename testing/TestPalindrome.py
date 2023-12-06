import unittest
from pda.palindrome import PalindromePDA
from pda.Simulator import input_string
from lexer.lexer import lexer

class Token:
    def __init__(self, t_type):
        self.type = t_type

class TestPalindromePDA(unittest.TestCase):
    def setUp(self):
        self.pda = PalindromePDA()

    def test_empty_string(self):
        result = self.pda.process_tokens([])
        print(f"Empty string test: {'Passed' if result else 'Failed'}")
        self.assertTrue(result)

    def test_even_palindromes(self):
        palindromes = ['AA', 'AAAA', 'AAAAAA', 'AABBAA', 'ABAABA', 'ABBA', 'ABBBBA', 'BAAAAB', 'BAAB', 'BABBAB', 'BB', 'BBAABB', 'BBBB', 'BBBBBB']
        for string in palindromes:
            tokens = [Token(char) for char in string]  # Crear tokens como objetos
            result = self.pda.process_tokens(tokens)
            print(f"Even palindrome '{string}' test: {'Passed' if result else 'Failed'}")
            self.assertTrue(result, f"Failed on string: {string}")

    def test_non_palindromes(self):
        non_palindromes = ['A', 'AAA', 'AAAB', 'ABAB', 'BABA']
        for string in non_palindromes:
            tokens = [Token(char) for char in string]  # Crear tokens como objetos
            result = self.pda.process_tokens(tokens)
            print(f"Non-palindrome '{string}' test: {'Passed' if not result else 'Failed'}")
            self.assertFalse(result, f"Failed on string: {string}")

    # Aquí puedes agregar más pruebas, como por ejemplo para probar la detección de caracteres ilegales
    def test_illegal_characters(self):
        illegal_strings = ['AC', 'aBc', '123', '!@#']
        for string in illegal_strings:
            lexer.illegal_characters = []  # Reinicia la lista de caracteres ilegales
            tokens, illegal_character_found = input_string(lexer, string)

            # Verifica si se encontraron caracteres ilegales
            self.assertTrue(illegal_character_found,
                            f"No illegal characters detected in string '{string}' but expected.")
            if illegal_character_found:
                print(
                    f"Testing illegal characters in string '{string}': Detected illegal characters - {' '.join(lexer.illegal_characters)}")
            else:
                print(f"Testing illegal characters in string '{string}': No illegal characters detected")


if __name__ == "__main__":
    unittest.main()
