def gcd1OfTwoNos(num1, num2):
    if (num1 == 0):
        return num2
    if (num2 == 0):
        return num1
    if (num1 == num2):
        return num1
    if (num1 > num2):
        return gcd1OfTwoNos(num1 - num2, num2)
    return gcd1OfTwoNos(num1, num2 - num1)


def Min_sum(arr, N):
    min_sum = 1000000
    maxgcd1 = 1
    for i in range(N):
        gcd1 = 1
        if (i == 0):
            gcd1 = arr[1]
        else:
            gcd1 = arr[i - 1]
        for j in range(N):
            if (j != i):
                gcd1 = gcd1OfTwoNos(gcd1, arr[j])
        c = arr[i]
        if (gcd1 > maxgcd1):
            maxgcd1 = gcd1
    return maxgcd1


if __name__ == '__main__':
    arr = [16, 5, 10, 25]
    N = len(arr)
    print(Min_sum(arr, N))
