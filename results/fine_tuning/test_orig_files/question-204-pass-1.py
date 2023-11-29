def numbers(n):

def numbers(n):
    count = 0
    for i in range(100, 1000):
        if str(i)[-n:] == str(i)[:n] and '3' in str(i) and '4' in str(i):
            count += 1
    return count
