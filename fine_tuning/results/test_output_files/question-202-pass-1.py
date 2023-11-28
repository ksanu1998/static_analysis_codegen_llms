def sum(n):
    if (n == 1):
        return 1
    else:
        res = (n ^ sum(n - 1))
        return res


if __name__ == "__main__":
    n = 5
    print(sum(n))
