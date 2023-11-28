def minOpsToEmptyString(s):
    ans = -10 ** 9
    cn0 = 0
    cn1 = 0
    for i in range(len(s)):
        if (s[i] == '0'):
            if (cn1 > 0):
                cn1 -= 1
            cn0 += 1
        else:
            if (cn0 > 0):
                cn0 -= 1
            cn1 += 1
        ans = max([ans, cn0, cn1])
    print(ans)


if __name__ == '__main__':
    S = "010101"
    minOpsToEmptyString(S)
