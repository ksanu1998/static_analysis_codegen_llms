def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        print("SET")
    else:
        print("NOT SET")


n = 5
k = 1
isKthBitSet(n, k)
