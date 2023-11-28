fib = []


class node:
    def __init__(self, data):
        self .data = data
        self .left = None
        self .right = None


def newNode(data):
    temp = node(data)
    return temp


def height(root):
    ht = 0
    if (root is None):
        return 0
    return (max(height(root .left), height(root .right)) + 1)


def FibonacciSeries(n):
    fib .append(0)
    fib .append(1)
    for i in range(2, n):
        fib .append(fib[i - 1] + fib[i - 2])


def CountPathUtil(root, i, count):
    if (root is None or not (fib[i] == root .data)):
        return count
    if (not root .left and not root .right):
        count += 1
    count = CountPathUtil(root .left, i + 1, count)
    return CountPathUtil(root .right, i + 1, count)


def CountPath(root):
    ht = height(root)
    FibonacciSeries(ht)
    print(CountPathUtil(root, 0, 0))


if __name__ == '__main__':
    root = newNode(0)
    root .left = newNode(1)
    root .right = newNode(1)
    root .left .left = newNode(1)
    root .left .right = newNode(4)
    root .right .right = newNode(1)
    root .right .right .left = newNode(2)
    CountPath(root)
