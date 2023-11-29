import math


def primeFactors(n, freq):
    freq[0] = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            freq[i] += 1
            freq[0] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if (freq[i]!= 0):
            freq[i] = 1


def main():
    freq = [0] * 100
    primeFactors(12, freq)
    print(freq)


if __name__ == "__main__":
    main()
