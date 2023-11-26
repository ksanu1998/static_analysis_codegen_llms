from collections import defaultdict


def countPairs(arr, N):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] * j == arr[j] * i:
                count += 1
    return count
