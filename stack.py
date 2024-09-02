class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def empty(self):
        return self.data == []

    def size(self):
        return len(self.data)

    def pop(self):
        if not Stack.empty(self):
            return self.data.pop()

        print('\npop(): empty stack error\n')

    def peek(self):
        if not Stack.empty(self):
            print(f'Top: {self.data[Stack.size(self) - 1]}')

            return None

        print(f'\npeek(): empty stack error\n')

    def print_stack(self):
        print('Stack: ', end = '')

        for value in self.data:
            print(f'{value} ', end = '')

        print('\n')