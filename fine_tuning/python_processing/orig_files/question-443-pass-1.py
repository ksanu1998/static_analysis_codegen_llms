def possibleEqualArray(A, N):
    tot_XOR = 0
    for i in range(N):
        tot_XOR ^= A[i]
    if (tot_XOR == 0):
        print("YES")
        return
    cur_XOR = 0
    cnt = 0
    for i in range(N):
        cur_XOR ^= A[i]
        if (cur_XOR == tot_XOR):
            cnt += 1
            cur_XOR = 0
    if (cnt > 2):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    A = [0, 2, 2]
    N = len(A)
    possibleEqualArray(A, N)
