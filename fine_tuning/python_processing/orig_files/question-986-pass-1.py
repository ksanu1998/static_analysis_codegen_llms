import math


def isPower(n):
    p = 0
    if (n <= 1):
        return 1
    for i in range(2, (int)(math .sqrt(n)) + 1):
        p = math .log2(n) / math .log2(i)
        if ((math .ceil(p) == math .floor(p)) and p > 1):
            return 1
    return 0


for i in range(2, 100):
    if isPower(i):
        print(i, end=" ")
