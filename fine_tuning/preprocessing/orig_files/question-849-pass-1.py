def calculateSum(n):
    sum = 0
    for row in range(n):
        sum = sum + (1 << row)
    return sum


n = 10
print("Sum of all elements:", calculateSum(n))
