def CountOfTriplets(a, n):
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if a[i] ^ a[j] == a[j+1]:
                count += 1
    return count
