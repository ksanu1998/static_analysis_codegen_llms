from array import *
from math import *


def countOddIntegers(arr, N):
    count = 0
    for i in range(N):
        if arr[i] % 2!= 0:
            count += 1
    return count
