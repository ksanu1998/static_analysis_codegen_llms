from math import sqrt, pow


def isPerfectPower(n):
    if (n == 1):
        return 1
    for i in range(1, int(sqrt(n)) + 1):
        if (pow(i, 2) == n):
            return 1
    return 0


if __name__ == "__main__":
    n = 10
    if (isPerfectPower(n)):
        print("Yes")
    else:
        print("No")
