fib = []


class node:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None


def count_fibonacci_paths(root):
    if root is None:
        return 0

    left = count_fibonacci_paths(root.left)
    right = count_fibonacci_paths(root.right)

    fib.append(left + right)

    return left + right


def print_fibonacci_sequence():
    for i in range(len(fib)):
        print(fib[i])


def main():
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    count_fibonacci_paths(root)
    print_fibonacci_sequence()


if __name__ == "__main__":
    main()
```
This code defines a class `node` that represents a node in a binary tree, and a function `count_fibonacci_paths` that counts the number of Fibonacci paths in a binary tree. The function uses a global variable `fib` to store the Fibonacci numbers. The function also uses a recursive approach to traverse the binary tree and count the Fibonacci paths.

The `main` function creates a binary tree with the given structure and calls
