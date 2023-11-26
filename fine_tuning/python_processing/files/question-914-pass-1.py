def countDigitOne(n):
    count = 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        n = n // 10
    return count
