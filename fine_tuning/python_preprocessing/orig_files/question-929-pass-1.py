import math


def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def checkCircular(N):
    count = 0
    temp = N
    while (temp > 0):
        count = count + 1
        temp = temp / 10
    num = N
    while (isPrime(num)):
        rem = num % 10
        div = num / 10
        num = (int)((math .pow(10, count - 1)) * rem) + div
        if (num == N):
            return True
    return False


N = 1193
if (checkCircular(N)):
    print "Yes"
else:
    print "No"
