from pda.Simulator import simulate_pda

# main.py
if __name__ == "__main__":
    while True:
        user_input = input("Ingresa una cadena (o escribe 'X' para salir): ")
        if user_input.upper() == 'X':
            break
        simulate_pda(user_input)

