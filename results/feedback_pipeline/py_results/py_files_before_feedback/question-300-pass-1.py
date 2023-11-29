def count_numbers(n):
    count = 0
    for i in range(1, 10**n):
        if str(i).count("0") % 2 == 1:
            count += 1
    return count