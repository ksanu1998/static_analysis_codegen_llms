from operator import xor


def findXOR(n):
    res = 0
    for i in range(1, n + 1):
        res = xor(res, i)
    return res


if __name__ == "__main__":
    n = 10
    print(findXOR(n))
