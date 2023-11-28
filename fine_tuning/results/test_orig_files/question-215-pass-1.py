def maxAND(L, R):

def maxAND(L, R):
    max_val = 0
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            if (i & j) > max_val:
                max_val = i & j
    return max_val
