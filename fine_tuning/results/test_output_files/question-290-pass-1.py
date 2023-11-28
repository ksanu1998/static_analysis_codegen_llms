def numberOfDivisors(num):
    if (num == 1):
        return 1
    if (num == 2):
        return 2
    if (num == 3):
        return 3
    if (num == 4):
        return 4
    if (num == 5):
        return 5
    if (num == 6):
        return 6
    if (num == 7):
        return 7
    if (num == 8):
        return 8
    if (num == 9):
        return 9
    return 0


if __name__ == "__main__":
    n = 9
    print(numberOfDivisors(n))
