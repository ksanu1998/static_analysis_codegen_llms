def maxAND(L, R):
    return max(x & y for x in range(L, R+1) for y in range(x, R+1))
