# palindrome.py
from pda.stack import Stack

class PalindromePDA:
    def __init__(self):
        self.stack = Stack()
        self.current_state = 's'

    def process_token(self, token, index, total_length):
        half_length = total_length // 2

        # Rechazar cadenas de longitud impar
        if total_length % 2 != 0:
            self.current_state = 'rejected'
            return

        # Procesar la primera mitad
        if index < half_length:
            self.stack.push(token)
        # Procesar la segunda mitad
        elif index >= half_length:
            if not self.stack.is_empty() and self.stack.peek() == token:
                self.stack.pop()
            else:
                self.current_state = 'rejected'
                return

        # Verificar la pila al final
        if index == total_length - 1:
            if self.stack.is_empty():
                self.current_state = 'f'
            else:
                self.current_state = 'rejected'

    def get_current_state(self):
        return self.current_state

    def get_stack_contents(self):
        return ''.join(self.stack.items)

