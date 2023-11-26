def ans(n):
    if (n < 6):
        return n
    return n % 6 + 10 * (ans(n // 6)) - 1


def getSpecialNumber(N):
    return ans(N)


if __name__ == '__main__':
    N = 17
    answer = getSpecialNumber(N)
    print(answer)
