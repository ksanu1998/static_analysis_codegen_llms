import math


def countdigits(N):
    count = 0
    while (N):
        count = count + 1
        N = int(math .floor(N / 10))
    return count


def cyclic(N):
    num = N
    n = countdigits(N)
    while (1):
        print(int(num))
        rem = num % 10
        div = math .floor(num / 10)
        num = ((math .pow(10, n - 1)) * rem + div)
        if (num == N):
            break


N = 5674
cyclic(N)
