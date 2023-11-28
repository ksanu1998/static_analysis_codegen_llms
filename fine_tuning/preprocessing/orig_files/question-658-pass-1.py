import math


class Node:
    def __init__(self, key):
        self .key = key
        self .left = None
        self .right = None


def newNode(key):
    temp = Node(key)
    return temp


def find_x(n):
    if n == 1:
        return 1
    num = math .log10(n)
    x, no = 0, 0
    for i in range(2, n + 1):
        den = math .log10(i)
        p = num / den
        no = int(pow(i, int(p)))
        if abs(no - n) < 1e-6:
            x = i
            break
    return x


def is_key(n, x):
    p = math .log10(n) / math .log10(x)
    no = int(pow(x, int(p)))
    if n == no:
        return True
    return False


def evenPaths(node, count, x):
    if node is None or not is_key(node .key, x):
        return count
    if node .left is None and node .right is None:
        count += 1
    count = evenPaths(node .left, count, x)
    return evenPaths(node .right, count, x)


def countExpPaths(node, x):
    return evenPaths(node, 0, x)


root = newNode(27)
root .left = newNode(9)
root .right = newNode(81)
root .left .left = newNode(3)
root .left .right = newNode(10)
root .right .left = newNode(70)
root .right .right = newNode(243)
root .right .right .left = newNode(81)
root .right .right .right = newNode(909)
x = find_x(root .key)
print(countExpPaths(root, x))
