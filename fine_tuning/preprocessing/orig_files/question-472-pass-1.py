def find_Min_Inversion(n, s1, s2):
    count = 0
    s1 = list(s1)
    s2 = list(s2)
    for i in range(n - 1):
        if (s1[i] != s2[i]):
            if (s1[i] == '1'):
                s1[i] = '0'
            else:
                s1[i] = '1'
            if (s1[i + 1] == '1'):
                s1[i + 1] = '0'
            else:
                s1[i + 1] = '1'
            count += 1
    s1 = ''.join(s1)
    s2 = ''.join(s2)
    if (s1 == s2):
        return count
    return -1


if __name__ == '__main__':
    n = 4
    s1 = "0101"
    s2 = "1111"
    print(find_Min_Inversion(n, s1, s2))
