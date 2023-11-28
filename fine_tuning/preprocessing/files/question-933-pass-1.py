def countDigits(a, b):
    product = a * b
    count = 0
    while product > 0:
        count += 1
        product //= 10
    return count
