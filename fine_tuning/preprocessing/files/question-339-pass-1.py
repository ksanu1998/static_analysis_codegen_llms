C = 5
R = 3
INT_MAX = 10000000
table = [[0 for i in range(C)]for j in range(R)]
visited = [[0 for i in range(C)]for j in range(R)]


def min(p, q, r, s):
    if p < q and p < r and p < s:
        return p
    elif q < p and q < r and q < s:
        return q
    elif r < p and r < q and r < s:
        return r
    else:
        return s
