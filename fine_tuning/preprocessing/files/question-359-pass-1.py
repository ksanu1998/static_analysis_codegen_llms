def solve(x):
    count = 0
    for i in range(10):
        if str(i) == str(i*x)[-1]:
            count += 1
    return count
