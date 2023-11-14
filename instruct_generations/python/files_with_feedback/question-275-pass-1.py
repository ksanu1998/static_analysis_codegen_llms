def largestNumber(n):
    digits = []
    for i in range(1, n+1):
        if i % 2 == 1:
            digits.append(i)
    return int("".join(map(str, digits)))
