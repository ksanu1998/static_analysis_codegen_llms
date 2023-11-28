def factorialWithoutMul(N):
    ans = N
    i = N - 1
    while (i > 0):
        sum = 0
        for j in range(i):
            sum += ans
        ans = sum
        i -= 1
    return ans


if __name__ == '__main__':
    N = 5
    print(factorialWithoutMul(N))
