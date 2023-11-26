def number0f2s(n):
    count = 0
    while (n > 0):
        if (n % 10 == 2):
            count = count + 1
        n = n // 10
    return count


def numberOf2sinRange(n):
    count = 0
    for i in range(2, n + 1):
        count = count + number0f2s(i)
    return count


print(numberOf2sinRange(22))
print(numberOf2sinRange(100))
