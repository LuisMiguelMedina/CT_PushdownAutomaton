from .palindrome import PalindromePDA
from ..lexer.lexer import begin_lexing

def input_string(lexer, string):
    begin_lexing(string)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    if hasattr(lexer, 'illegal_characters') and lexer.illegal_characters:
        print(f"Illegal characters found: {' '.join(lexer.illegal_characters)}")
        return None, True  # Retorna None y True para indicar que se encontraron caracteres ilegales

    return tokens, False


def simulate_pda(lexer):
    pda = PalindromePDA()
    while True:
        user_input = input("Enter a string (or 'X' to exit): ")
        if user_input.upper() == 'X':
            break
        tokens, illegal_character_found = input_string(lexer, user_input)
        if illegal_character_found:
            print("String rejected: Illegal characters found.")
            continue
        if len(tokens) % 2 != 0:
            print("String rejected: The length of the string is not even.")
            continue
        if pda.process_tokens(tokens):
            print("String accepted: It is an even-length palindrome.")
        else:
            print("String rejected: It is not an even-length palindrome.")
        pda.stack.reset()  # Reset the stack for the next simulation
