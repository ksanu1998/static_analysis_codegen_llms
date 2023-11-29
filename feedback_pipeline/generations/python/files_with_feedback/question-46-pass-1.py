def count(a, n):
    count = 0
    for i in range(1, n + 1):
        if a[i] % a[i - 1]!= 0 and a[i] % a[i + 1]!= 0:
            count += 1
    return count
