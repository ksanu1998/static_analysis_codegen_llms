import sys
INT_MAX = sys .maxsize



def countDistinct(n):
    count = 0
    while n > 0:
        if n % 10 not in [1, 4, 7]:
            count += 1
        n //= 10
    return count
