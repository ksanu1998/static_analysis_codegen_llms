def countDecreasing(A, n):
    len = 1
    for i in range(n - 1):
        if (A[i + 1] < A[i]):
            len += 1
        else:
            cnt += (((len - 1) * len) // 2)
            len = 1
    if (len > 1):
        cnt += (((len - 1) * len) // 2)
    return cnt


if __name__ == "__main__":
    A = [100, 3, 1, 13]
    n = len(A)
    print(countDecreasing(A, n))
