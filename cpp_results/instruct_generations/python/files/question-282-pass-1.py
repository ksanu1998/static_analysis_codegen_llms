def divisor(a):
    count = 0
    for i in range(1, a + 1):
        if i % 2!= 0:
            count += 1
    return count