# Check if Matrix sum is prime or not. 
import math


def isPrime(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
    return True


def isPrimeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isPrime(matrix[i][j]):
                return False
    return True


def getPrimeMatrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(math.ceil(math.sqrt(i * j)))
        matrix.append(row)
    return matrix


def main():
    n = int(input())
    matrix = getPrimeMatrix(n)
    if isPrimeMatrix(matrix):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()




















































































































































































