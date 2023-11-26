def summ(arr, N, K):
    sum = 4
    v = [i for i in arr]
    for i in range(len(v)):
        if (v[i] % K == 0):
            x = v[i] // K
            for j in range(K):
                v .append(x)
        else:
            break
    for i in range(len(v)):
        sum = sum + v[i]
    return sum


if __name__ == '__main__':
    arr = [4, 6, 8, 2]
    K = 2
    N = len(arr)
    print(summ(arr, N, K))
