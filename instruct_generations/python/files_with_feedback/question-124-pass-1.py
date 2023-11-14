import sys
INT_MAX = sys .maxsize


def count_distinct(n):
    count = 0
    for i in range(1, n+1):
        if len(set(str(i))) == len(str(i)):
            count += 1
    return count
