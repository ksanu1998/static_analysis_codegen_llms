import math


def insertPF(primeFact, fact):
    for i in range(len(primeFact)):
        if (primeFact[i] == 0):
            primeFact[i] = fact


def isPrime(n):
    if (n == 1):
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return 0
    return 1


def main():
    primeFact = [0] * 100
    insertPF(primeFact, 2)
    for i in range(3, 100, 2):
        if (isPrime(i)):
            insertPF(primeFact, i)
    for i in range(1, 100):
        if (primeFact[i] == 0):
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
