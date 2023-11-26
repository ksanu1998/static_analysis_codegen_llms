def count(a, b):
    count = 0
    for i in range(len(a)):
        if a[i:].startswith(b):
            count += 1
    return count
