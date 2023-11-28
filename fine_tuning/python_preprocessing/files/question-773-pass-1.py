import math


def cntPairs(arr, N):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (arr[i] & arr[j]) > (arr[i] ^ arr[j]):
                count += 1
    return count
