def minTrees(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1
    return count


if __name__ == '__main__':
    n = 7
    print(minTrees(n))
