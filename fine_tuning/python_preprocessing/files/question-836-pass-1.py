import heapq


def minCost(arr, n):
    if n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] + arr[1]
    else:
        return min(arr[0] + minCost(arr[1:], n-1), arr[1] + minCost(arr[2:], n-2))
