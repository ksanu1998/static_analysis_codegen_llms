def is_lexicographically_smaller(a, b):
    for i in range(len(a)):
        if a[i]!= b[i]:
            return a[i] < b[i]
    return len(a) < len(b)
