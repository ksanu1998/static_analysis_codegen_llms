import math
N = 100001
adj = [[]for i in range(N)]
a = [0 for i in range(N)]
ans = [0 for i in range(N)]



def hasOddNumberOfDivisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 1
