MAX = 10000
CHAR_SIZE = 26


def precompute(mat, str, Len):
    for i in range(CHAR_SIZE):
        mat[Len][i] = Len
    for i in range(Len - 1, -1, -1):
        for j in range(CHAR_SIZE):
            mat[i][j] = mat[i + 1][j]
        mat[i][ord(str[i]) - ord('a')] = i


def query(mat, str, Len):
    pos = 0
    for i in range(len(str)):
        if (mat[pos][ord(str[i]) - ord('a')] >= Len):
            return False
        else:
            pos = mat[pos][ord(str[i]) - ord('a')] + 1
    return True


S = "geeksforgeeks"
Len = len(S)
mat = [[0 for i in range(CHAR_SIZE)]for j in range(MAX)]
precompute(mat, S, Len)
get = "No"
if (query(mat, "gg", Len)):
    get = "Yes"
print(get)
get = "No"
if (query(mat, "gro", Len)):
    get = "Yes"
print(get)
get = "No"
if (query(mat, "gfg", Len)):
    get = "Yes"
print(get)
get = "No"
if (query(mat, "orf", Len)):
    get = "Yes"
print(get)
