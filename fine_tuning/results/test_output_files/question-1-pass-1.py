import math


def sumOfTwoCubes(n):
    for i in range(1, int(math.sqrt(n))):
        j = int(math.pow(n - i, 1.0 / 3))
        if (i * i * i + j * j * j == n):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    sumOfTwoCubes(12)
