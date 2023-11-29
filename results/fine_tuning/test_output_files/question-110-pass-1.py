import math


def minOperations(A, B):
    n = math.ceil(math.log2(B))
    if (A > B):
        print(n)
    else:
        print(n - 1)


A = 1
B = 2
minOperations(A, B)
A = 1
B = 3
minOperations(A, B)
A = 2
B = 3
minOperations(A, B)
A = 1
B = 4
minOperations(A, B)
A = 2
B = 4
minOperations(A, B)
A = 3
B = 4
minOperations(A, B)
A = 1
B = 5
minOperations(A, B)
A = 2
B = 5
minOperations(A, B)
A = 3
B = 5
minOperations(A, B)
A = 4
B = 5
minOperations(A, B)
