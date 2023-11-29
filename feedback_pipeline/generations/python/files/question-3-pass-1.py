def findNthNumber(N):
    nth_number = 1
    for i in range(N):
        nth_number = nth_number * 10
        if nth_number % 9 == 0:
            nth_number = nth_number // 9
    return nth_number