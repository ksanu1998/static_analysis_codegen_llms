def gcd(a, b):
    if ((a % b) == 0):
        return b
    return gcd(b, a % b)


def firstFactorialDivisibleNumber(x):
    new_x = x
    for i in range(1, x):
        new_x /= gcd(i, new_x)
        if (new_x == 1):
            break
    return i


def main():
    x = 16
    print(firstFactorialDivisibleNumber(x))


if __name__ == '__main__':
    main()
