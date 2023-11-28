def countDigitOne(n):
    countr = 0
    for i in range(1, n + 1):
        str1 = str(i)
        countr += str1 .count("1")
    return countr


n = 13
print(countDigitOne(n))
n = 131
print(countDigitOne(n))
n = 159
print(countDigitOne(n))
