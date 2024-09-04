class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        new_node = Node()
        new_node.data = val
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.empty():
            print('\npop(): empty stack\n')

            return None

        return_val = self.top.data
        node_rm = self.top
        self.top = self.top.next
        self.size -= 1

        del node_rm
        return return_val

    def empty(self):
        return self.top == None

    def get_size(self):
        return self.size

    def peek(self):
        if self.empty():
            print('\npeek(): empty stack\n')

            return None

        return self.top.data

    def print_stack(self):
        if self.empty():
            return None

        print('Stack: ', end='')
        node_aux = self.top

        while node_aux != None:
            print(f'{node_aux.data} -> ', end='')

            node_aux = node_aux.next

        print('NULL')