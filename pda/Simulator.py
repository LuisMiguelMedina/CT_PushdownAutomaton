from pda.palindrome import PalindromePDA
from lexer.lexer import begin_lexing

def simulate_pda(string):
    tokens, illegal_characters = begin_lexing(string)
    token_values = [token.value for token in tokens]

    pda = PalindromePDA()
    print("{:<15} {:<15} {:<15}".format('Estado', 'Por leer', 'Pila'))

    for i, token in enumerate(token_values):
        pda.process_token(token, i, len(token_values))
        current_state = pda.get_current_state()
        char_remaining = string[i+1:]
        stack_contents = pda.get_stack_contents()
        print("{:<15} {:<15} {:<15}".format(current_state, char_remaining, stack_contents))

    pda.finalize()

    if illegal_characters:
        print("Caracteres ilegales encontrados:", ", ".join(illegal_characters))

    final_state = pda.get_current_state()
    if final_state == 'f':
        print("Cadena aceptada: Es un palindromo de longitud par")
    else:
        print("Cadena rechazada: No es un palindromo de longitud par o contiene caracteres ilegales")
