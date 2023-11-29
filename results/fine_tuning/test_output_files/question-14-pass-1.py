from math import sqrt, ceil, floor


def constructArrayWithGivenLCM(N):
    LCM = 1
    for i in range(1, N + 1):
        LCM = (LCM * i) // gcd(LCM, i)
    print(LCM)
    arr = [1] * N
    for i in range(1, N):
        arr[i] = (LCM // i)
    for i in range(N - 1, -1, -1):
        for j in range(1, N + 1):
            if (arr[i] >= j):
                arr[i] -= j
                break
    for i in range(N):
        print(arr[i], end=" ")


if __name__ == "__main__":
    N = 5
    constructArrayWithGivenLCM(N)
