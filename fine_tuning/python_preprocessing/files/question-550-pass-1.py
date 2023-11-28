def printMatrix(n, m):
    vowels = ['a', 'e', 'i', 'o', 'u']
    matrix = [[vowels[i % 5] for i in range(n)] for j in range(m)]
    return matrix
