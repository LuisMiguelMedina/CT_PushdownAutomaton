from pda.Simulator import simulate_pda

# main.py
if __name__ == "__main__":
    while True:
        user_input = input("Enter a string (or 'X' to exit): ")
        if user_input.upper() == 'X':
            break
        simulate_pda(user_input)

