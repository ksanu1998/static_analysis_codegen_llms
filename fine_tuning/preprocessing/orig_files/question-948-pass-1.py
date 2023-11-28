def countDigit(n):
    temp = n
    count = 0
    while temp != 0:
        d = temp % 10
        temp //= 10
        if d > 0 and n % d == 0:
            count += 1
    return count


n = 1012
print(countDigit(n))
