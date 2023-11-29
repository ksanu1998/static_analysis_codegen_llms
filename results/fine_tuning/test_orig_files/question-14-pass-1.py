from math import sqrt, ceil, floor



def constructArrayWithGivenLCM(N):
    # Find the greatest common divisor of 1 to N
    gcd = 1
    for i in range(2, N + 1):
        gcd = gcd.__gcd__(i)

    # Initialize the array with the greatest common divisor
    arr = [gcd] * N

    # Fill in the remaining elements
    for i in range(1, N):
        arr[i] = arr[i - 1] + gcd

    return arr
