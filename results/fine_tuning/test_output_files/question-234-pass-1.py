import math as mt


def findingValues(m, n, mth, nth):
    if (mth == 1):
        print(m * (m + 1) // 2)
    else:
        if (mth == 2):
            print(m * (m + 1) // 2 - n * (n + 1) // 2)
        else:
            print(m * (m + 1) // 2 - n * (n + 1) // 2 + n * (n + 1) // 2)


if __name__ == "__main__":
    m = 1
    n = 2
    mth = 2
    nth = 3
    findingValues(m, n, mth, nth)
