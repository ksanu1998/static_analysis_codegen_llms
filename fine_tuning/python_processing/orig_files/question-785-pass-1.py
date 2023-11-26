import math


def solve(A, n, Q, q):
    one = 0
    for i in range(0, n):
        if (A[i] == 1):
            one += 1
    glows = 0
    count = 0
    if (one >= int(math .ceil(n / 2))):
        glows = 1
    for i in range(0, q):
        prev = glows
        if (A[Q[i] - 1] == 1):
            one -= 1
        if (A[Q[i] - 1] == 0):
            one += 1
        A[Q[i] - 1] ^= 1
        if (one >= int(math .ceil(n / 2.0))):
            glows = 1
        else:
            glows = 0
        if (prev != glows):
            count += 1
    return count


n = 3
arr = [1, 1, 0]
q = 3
Q = [3, 2, 1]
print(solve(arr, n, Q, q))
