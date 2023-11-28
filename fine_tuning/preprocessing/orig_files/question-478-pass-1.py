def countStringPairs(a, n):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n, 1):
            p = a[i]
            q = a[j]
            if (p[0] != q[0]):
                p = list(p)
                q = list(q)
                temp = p[0]
                p[0] = q[0]
                q[0] = temp
                p = ''.join(p)
                q = ''.join(q)
                flag1 = 0
                flag2 = 0
                for k in range(n):
                    if (a[k] == p):
                        flag1 = 1
                    if (a[k] == q):
                        flag2 = 1
                if (flag1 == 0 and flag2 == 0):
                    ans = ans + 1
    print(ans)


if __name__ == '__main__':
    arr = ["good", "bad", "food"]
    N = len(arr)
    countStringPairs(arr, N)
