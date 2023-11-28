def updateString(S, A, B):
    l = len(A)
    i = 0
    while i + l <= len(S):
        curr = S[i:i + l]
        if curr == A:
            new_string = S[0:i] + B + S[i + l:len(S)]
            S = new_string
            i += l - 1
        else:
            new_string = S[0:i] + A + S[i + l:len(S)]
            S = new_string
            i += l - 1
        i += 1
    return S


if __name__ == "__main__":
    S = "aab"
    A = "aa"
    B = "bb"
    print(updateString(S, A, B))
