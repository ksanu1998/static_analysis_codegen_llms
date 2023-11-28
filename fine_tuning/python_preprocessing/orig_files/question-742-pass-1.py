def findIfPossible(N, S, X):
    if (S >= X and S % 2 == X % 2):
        if (N >= 3):
            return "Yes"
        if (N == 1):
            if (S == X):
                return "Yes"
            else:
                return "No"
        if (N == 2):
            C = (S - X) // 2
            A = C
            B = C
            A = A + X
            if (((A ^ B) == X)):
                return "Yes"
            else:
                return "No"
    else:
        return "No"


N = 3
S = 10
X = 4
print(findIfPossible(N, S, X))
