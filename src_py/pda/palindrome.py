from pda.stack import Stack

PDAstack = Stack()

class PalindromePDA:
    def __init__(self):
        self.stack = PDAstack

    def process_tokens(self, tokens):
        for index, token in enumerate(tokens):
            if index < len(tokens) / 2:
                self.stack.push(token.type)
            else:
                # En la segunda mitad, cada token debe coincidir con el tope de la pila
                if self.stack.is_empty() or self.stack.peek() != token.type:
                    return False
                self.stack.pop()

        # La cadena es un palíndromo si la pila está vacía al final
        return self.stack.is_empty()
