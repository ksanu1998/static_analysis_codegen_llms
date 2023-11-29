def divide(a, b):
    c = 1
    for i in range(1, a + 1):
        if (a % i == 0 and b % i == 0):
            c = i
    print(a / c, b / c)


if __name__ == "__main__":
    divide(12, 18)
