from pda.palindrome import PalindromePDA


def input_string(lexer):
    user_input = input("Enter a string (or 'X' to exit): ")
    if user_input.upper() == 'X':
        return None, True
    lexer.input(user_input.lower())  # Convertir a minúsculas para manejar la entrada de manera uniforme
    tokens = []
    illegal_character_found = False
    while True:
        tok = lexer.token()
        if not tok:  # No hay más tokens
            break
        if tok.type not in {"A", "B"}:  # Verificamos si el token es un caracter válido
            illegal_character_found = True
            print(f"Illegal character '{tok.value}'")
        tokens.append(tok)
    return tokens, illegal_character_found


def simulate_pda(lexer):
    pda = PalindromePDA()
    while True:
        tokens, illegal_character_found = input_string(lexer)
        if tokens is None:  # El usuario ingresó 'X' para salir
            break
        if illegal_character_found:  # Si se encontraron caracteres ilegales
            print("String rejected: Illegal characters found.")
            continue
        if len(tokens) % 2 != 0:  # Rechazar si la longitud no es par
            print("String rejected: The length of the string is not even.")
            continue
        if pda.process_tokens(tokens):
            print("String accepted: It is an even-length palindrome.")
        else:
            print("String rejected: It is not an even-length palindrome.")
        pda.stack.items.clear()  # Reset the stack for the next simulation
