class StackWithMax:
    def __init__(self):
        self .mainStack = []
        self .trackStack = []

    def push(self, x):
        self .mainStack .append(x)
        if (len(self .mainStack) == 1):
            self .trackStack .append(x)
            return
        if (x > self .trackStack[-1]):
            self .trackStack .append(x)
        else:
            self .trackStack .append(self .trackStack[-1])

    def getMax(self):
        return self .trackStack[-1]

    def pop(self):
        self .mainStack .pop()
        self .trackStack .pop()


if __name__ == '__main__':
    s = StackWithMax()
    s .push(20)
    print(s .getMax())
    s .push(10)
    print(s .getMax())
    s .push(50)
    print(s .getMax())
