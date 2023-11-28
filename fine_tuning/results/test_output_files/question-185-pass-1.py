def findX(A, B):
    n = len(A)
    X = 0
    for i in range(n):
        X ^= (A[i] ^ B[i])
    return X


A = [1, 2, 3, 4, 5]
B = [2, 3, 4, 5, 6]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 5]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 6]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 7]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 8]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 9]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 10]
print(findX(A, B))
A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 11]
print(findX(A, B))
A = [1, 2, 3
