import math


def count_ht(s, N):
    heads = 0
    tails = 0
    for i in range(N):
        if s[i] == 'H':
            heads += 1
        else:
            tails += 1
    return (heads, tails)
