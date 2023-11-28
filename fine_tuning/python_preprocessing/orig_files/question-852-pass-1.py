def countOnes(n):
    count = 1
    rem = 1
    while (rem != 0):
        rem = (rem * 10 + 1) % n
        count = count + 1
    return count


n = 13
print(countOnes(n))
