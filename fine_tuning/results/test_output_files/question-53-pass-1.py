def isPossible(A, B):
    if (A < B):
        return 0
    for i in range(2, A + 1):
        if (A % i == 0 and B % i == 0):
            return 1
    return 0


if __name__ == "__main__":
    A = 12
    B = 15
    if (isPossible(A, B)):
        print("Yes")
    else:
        print("No")
