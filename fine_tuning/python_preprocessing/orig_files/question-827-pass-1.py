BOUND = 4
top = -1
a = []
length = 0


def create_new():
    global length
    new_a = [0 for i in range(length + BOUND)]
    for i in range(length):
        new_a[i] = a[i]
    length += BOUND
    return new_a


def push(element):
    global top, a
    if (top == length - 1):
        a = create_new()
    top += 1
    a[top] = element
    return a


def pop():
    global top
    top -= 1


def display():
    global top
    if (top == -1):
        print("Stack is Empty")
    else:
        print("Stack: ", end='')
        for i in range(top + 1):
            print(a[i], end=' ')
        print()


if __name__ == '__main__':
    a = create_new()
    push(1)
    push(2)
    push(3)
    push(4)
    display()
    push(5)
    push(6)
    display()
    push(7)
    push(8)
    display()
    push(9)
    display()
