def countOddSum(a, n):
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    return count
