from math import gcd as __gcd

def findLargest(arr, n):
    largest = 1
    for i in range(2, n+1):
        if __gcd(arr[i], largest) == 1:
            largest = arr[i]
    return largest
