def totalSumDivisibleByNum(digit, number):
    total = 0
    for i in range(1, 10**digit):
        if i % number == 0:
            total += i
    return total
