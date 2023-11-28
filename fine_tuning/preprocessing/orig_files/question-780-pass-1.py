def countSubsequences(A):
    odd = 0
    even = 0
    for el in A:
        if (el % 2 == 1):
            odd += 1
        else:
            even += 1
    if (odd == 0):
        print(0)
    else:
        print(1 << len(A) - 1)


if __name__ == "__main__":
    A = [1, 3, 4]
    countSubsequences(A)
