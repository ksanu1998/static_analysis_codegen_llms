def findNth(n):
    count = 0
    curr = 19
    while (True):
        sum = 0
        x = curr
        while (x > 0):
            sum = sum + x % 10
            x = int(x / 10)
        if (sum == 10):
            count += 1
        if (count == n):
            return curr
        curr += 9
    return -1


print(findNth(5))
