class Stack:
    def __init__(self):
        self .items = []

    def isEmpty(self):
        return self .items == []

    def push(self, item):
        self .items .append(item)

    def pop(self):
        return self .items .pop()

    def peek(self):
        return self .items[len(self .items) - 1]

    def size(self):
        return len(self .items)


def deleteMid(st, n, curr):
    if (st .isEmpty() or curr == n):
        return
    x = st .peek()
    st .pop()
    deleteMid(st, n, curr + 1)
    if (curr != int(n / 2)):
        st .push(x)


st = Stack()
st .push('1')
st .push('2')
st .push('3')
st .push('4')
st .push('5')
st .push('6')
st .push('7')
deleteMid(st, st .size(), 0)
while (st .isEmpty() == False):
    p = st .peek()
    st .pop()
    print(str(p) + " ", end="")
