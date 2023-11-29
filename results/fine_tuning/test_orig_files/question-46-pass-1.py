def count(a, n):

def count_elements(a, n):
    count = 0
    for i in range(1, n + 1):
        if a[i] % a[i - 1]!= 0:
            count += 1
    return count
