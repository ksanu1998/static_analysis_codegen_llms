from math import ceil, sqrt


def FermatFactors(n):
    if (n == 1):
        print(1)
        return
    a = ceil(sqrt(n))
    for i in range(2, a):
        if (n % i == 0):
            print(i)
            print(n // i)
            return
    print(n)


if __name__ == "__main__":
    FermatFactors(12)
