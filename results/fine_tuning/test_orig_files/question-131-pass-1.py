from math import gcd as __gcd



def findLargest(arr, n):
    largest = 1
    for i in range(2, n + 1):
        if __gcd(i, n) == 1:
            largest = i
            break
    return largest
