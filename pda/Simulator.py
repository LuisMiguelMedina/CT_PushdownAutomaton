# simulator.py
from pda.palindrome import PalindromePDA
from lexer.lexer import begin_lexing

def simulate_pda(string):
    tokens = begin_lexing(string)
    token_values = [token.value for token in tokens if token.type != 'ERROR']

    # Verificar longitud par y que no haya caracteres ilegales
    if len(string) % 2 != 0 or len(token_values) != len(tokens):
        print("String rejected: Invalid length or illegal characters.")
        return

    pda = PalindromePDA()
    print("{:<15} {:<15} {:<15}".format('Estado', 'Por leer', 'Pila'))

    for i, token in enumerate(token_values):
        pda.process_token(token, i, len(token_values))
        current_state = pda.get_current_state()
        char_remaining = string[i+1:]
        stack_contents = ''.join(pda.get_stack_contents())
        print("{:<15} {:<15} {:<15}".format(current_state, char_remaining, stack_contents))

    if pda.get_current_state() == 'f':
        print("String accepted: It is an even-length palindrome.")
    else:
        print("String rejected: It is not an even-length palindrome.")

# Nota: La función `simulate_pda` no se llama aquí, se debe llamar desde main.py
