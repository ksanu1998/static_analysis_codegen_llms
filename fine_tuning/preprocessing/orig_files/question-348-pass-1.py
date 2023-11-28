def MinOfCubed(k):
    if (k < 8):
        return k
    res = k
    for i in range(1, k + 1):
        if ((i * i * i) > k):
            return res
        res = min(res, MinOfCubed(k - (i * i * i)) + 1)
    return res


num = 15
print(MinOfCubed(num))
