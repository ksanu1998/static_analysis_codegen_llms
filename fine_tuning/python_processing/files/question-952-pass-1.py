def number0f2s(n):
    count = 0
    for i in range(n+1):
        if str(i).find('2')!= -1:
            count += 1
    return count
