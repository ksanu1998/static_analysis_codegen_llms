class Point:
    def __init__(self, a, b):
        self .x = a
        self .y = b


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def getCount(p, q):
    if p .x == q .x:
        return abs(p .y - q .y) - 1
    if p .y == q .y:
        return abs(p .x - q .x) - 1
    return gcd(abs(p .x - q .x), abs(p .y - q .y)) - 1


if __name__ == "__main__":
    p = Point(1, 9)
    q = Point(8, 16)
    print(
        "The number of integral points",
        "between ({}, {}) and ({}, {}) is {}".format(
            p .x,
            p .y,
            q .x,
            q .y,
            getCount(
                p,
                q)))
