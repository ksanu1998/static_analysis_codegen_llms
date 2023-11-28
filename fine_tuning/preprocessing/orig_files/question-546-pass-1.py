def minOperations(str, n):
    count = 0
    for i in range(n - 1):
        if (str[i] != str[i + 1]):
            count += 1
    return (count + 1) // 2


str = "000111"
n = len(str)
print(minOperations(str, n))
