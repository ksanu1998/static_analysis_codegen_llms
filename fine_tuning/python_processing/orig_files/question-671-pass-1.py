import math
import sys


def closestsAngle(N, A):
    mi = sys .maxsize
    ans = 0
    for i in range(N):
        angle = 180.0 * i / N
        if (math .fabs(angle - A) < math .fabs(mi - A)):
            mi = angle
            i += 1
            ans = i
    print(2, 1, 2 + ans)


if __name__ == '__main__':
    N = 3
    A = 15
    closestsAngle(N, A)
