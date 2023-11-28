def spellsCount(num):
    n = len(num)
    result = 1
    i = 0
    while (i < n):
        count = 1
        while (i < n - 1 and num[i + 1] == num[i]):
            count += 1
            i += 1
        result = result * int(pow(2, count - 1))
        i += 1
    return result


num = "11112"
print(spellsCount(num))
