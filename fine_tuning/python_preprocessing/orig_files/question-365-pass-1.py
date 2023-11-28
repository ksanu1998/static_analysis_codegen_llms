MAX = 10
F = [[-1 for i in range(MAX)]for j in range(MAX)]
C = [None] * MAX


def noOfAssignments(S, n, i, c_x):
    if F[i][c_x] != -1:
        return F[i][c_x]
    if i == n:
        F[i][c_x] = not c_x
        return F[i][c_x]
    c_y = C[i] - c_x
    if S[i] == '(':
        F[i][c_x] = noOfAssignments(
            S, n, i + 1, c_x + 1) + noOfAssignments(S, n, i + 1, c_x)
        return F[i][c_x]
    F[i][c_x] = 0
    if c_x:
        F[i][c_x] += noOfAssignments(S, n, i + 1, c_x - 1)
    if c_y:
        F[i][c_x] += noOfAssignments(S, n, i + 1, c_x)
    return F[i][c_x]


if __name__ == "__main__":
    S = "()"
    n = len(S)
    C[0] = 0
    for i in range(0, n):
        if S[i] == '(':
            C[i + 1] = C[i] + 1
        else:
            C[i + 1] = C[i] - 1
    print(noOfAssignments(S, n, 0, 0))
