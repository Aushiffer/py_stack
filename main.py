from stack import Stack

if __name__ == '__main__':
    opt = 0
    s = Stack()

    while opt != 6:
        s.print_stack()
    
        print('1: push')
        print('2: pop')
        print('3: size of the stack')
        print('4: is the stack empty?')
        print('5: peek')
        print('6: quit')
    
        opt = int(input())
    
        match opt:
            case 1:
                val = int(input('Input value for push(): '))
    
                s.push(val)
            case 2:
                s.pop()
            case 3:
                print(f'Size: {s.size()}')
            case 4:
                print(f'Empty: {s.empty()}')
            case 5:
                s.peek()