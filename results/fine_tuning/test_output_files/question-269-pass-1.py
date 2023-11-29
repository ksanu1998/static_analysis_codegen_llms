def getResult(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    result = 1
    for (i = 2; i <= n; i++)
        result = (result * (getResult(i - 1) + getResult(i))) % 1000000007;
    return result;


if __name__ == "__main__":
    n = 5
    print(getResult(n))
