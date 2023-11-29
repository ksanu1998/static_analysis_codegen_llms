def findX(A, B):
    n = len(A)
    X = 0
    for i in range(n):
        X ^= (A[i] ^ B[i])
    return X


A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 7]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 8]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 9]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 10]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 11]
print(findX(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 12]
print(findX(A, B))
A = [1, 2, 3, 4
