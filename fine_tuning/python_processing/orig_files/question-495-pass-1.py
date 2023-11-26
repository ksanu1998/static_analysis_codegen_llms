def rearrange(s):
    s1 = []
    s2 = []
    for x in s:
        if x .isalpha():
            s1 .append(x)
        else:
            s2 .append(x)
    n = len(s1)
    m = len(s2)
    if (abs(n - m) > 1):
        return "-1"
    i = 0
    j = 0
    k = 0
    flag = 0
    if (n >= m):
        flag = 1
    else:
        flag = 0
    while (i < n and j < m):
        if (flag):
            s[k] = s1[i]
            k += 1
            i += 1
        else:
            s[k] = s2[j]
            k += 1
            j += 1
        flag = not flag
    return "".join(s)


if __name__ == '__main__':
    str = "geeks2020"
    str1 = [i for i in str]
    print(rearrange(str1))
