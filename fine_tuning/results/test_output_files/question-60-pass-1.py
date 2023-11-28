import math


def divisorsSame(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            cnt += 2
    if (cnt % 2 == 0):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    divisorsSame(12)
