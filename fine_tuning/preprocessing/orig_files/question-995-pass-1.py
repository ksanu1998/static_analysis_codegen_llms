def ConstructList(Q):
    xor = 0
    ans = []
    for i in range(len(Q) - 1, -1, -1):
        if (Q[i][0] == 0):
            ans .append(Q[i][1] ^ xor)
        else:
            xor ^= Q[i][1]
    ans .append(xor)
    ans .sort()
    return ans


Q = [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]]
print(ConstructList(Q))
