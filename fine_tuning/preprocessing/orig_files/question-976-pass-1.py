from math import gcd


def isPossible(a, b, c):
    return (c % gcd(a, b) == 0)


if __name__ == '__main__':
    a = 3
    b = 6
    c = 9
    if (isPossible(a, b, c)):
        print("Possible")
    else:
        print("Not Possible")
    a = 3
    b = 6
    c = 8
    if (isPossible(a, b, c)):
        print("Possible")
    else:
        print("Not Possible")
    a = 2
    b = 5
    c = 1
    if (isPossible(a, b, c)):
        print("Possible")
    else:
        print("Not Possible")
