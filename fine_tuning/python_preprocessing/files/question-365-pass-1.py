MAX = 10
F = [[-1 for i in range(MAX)]for j in range(MAX)]
C = [None] * MAX


def noOfAssignments(S, n, i, c_x):
    if i == n:
        return 1
    if F[i][c_x]!= -1:
        return F[i][c_x]
    count = 0
    for j in range(i, n):
        if S[j] == 'X':
            count += noOfAssignments(S, n, j + 1, c_x + 1)
        else:
            count += noOfAssignments(S, n, j + 1, c_x)
    F[i][c_x] = count
    return count
