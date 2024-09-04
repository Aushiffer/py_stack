from stack import Stack

if __name__ == '__main__':
    opt = 0
    st = Stack()

    while opt != 6:
        st.print_stack()
    
        print('\n1: push')
        print('2: pop')
        print('3: size of the stack')
        print('4: is the stack empty?')
        print('5: peek')
        print('6: quit')
    
        opt = int(input())

        print('\n')
    
        match opt:
            case 1:
                val = input('Input value for the push() function: ')
    
                st.push(val)
            case 2:
                st.pop()
            case 3:
                print(f'Size: {st.get_size()}')
            case 4:
                print(f'Empty: {st.empty()}')
            case 5:
                print(f'Top: {st.peek()}')