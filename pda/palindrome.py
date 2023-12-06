from pda.stack import Stack

class PalindromePDA:
    def __init__(self):
        self.stack = Stack()
        self.current_state = 's'

    def process_token(self, token, index, total_length):
        half_length = total_length // 2
        if total_length % 2 != 0:
            self.current_state = 'rechazado'
            return

        if index < half_length:
            self.stack.push(token)
        elif self.stack.is_empty() or self.stack.peek() != token:
            self.current_state = 'rechazado'
            return
        else:
            self.stack.pop()

        if index == total_length - 1:
            self.current_state = 'f' if self.stack.is_empty() else 'rechazado'

    def get_current_state(self):
        return self.current_state

    def get_stack_contents(self):
        return ''.join(self.stack.items)

    def finalize(self):
        if self.current_state != 'rechazado' and self.stack.is_empty():
            self.current_state = 'f'
        else:
            self.current_state = 'rechazado'
