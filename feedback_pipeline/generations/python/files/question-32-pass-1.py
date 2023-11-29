from bisect import bisect_left


def numberOfPairs(a, b, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j]:
                count += 1
    return count