import math



def Triplets(n):
    count = 0
    for a in range(1, int(n ** 0.5) + 1):
        for b in range(a, n + 1):
            c = math.sqrt(a ** 2 + b ** 2)
            if c ** 2 == a ** 2 + b ** 2 and 1 <= a <= b <= c <= n:
                count += 1
    return count
