def count(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


def findSetBits(n):
    for i in range(n + 1):
        print(count(i), end=" ")


if __name__ == '__main__':
    n = 5
    findSetBits(n)
