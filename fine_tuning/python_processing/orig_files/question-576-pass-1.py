def countWays(s1, s2, n):
    a = b = c = d = 0
    result = 0
    for i in range(0, n, 1):
        if (s2[i] == '0'):
            if (s1[i] == '0'):
                c += 1
            else:
                d += 1
        else:
            if (s1[i] == '0'):
                a += 1
            else:
                b += 1
    result = a * d + b * c + c * d
    return result


if __name__ == '__main__':
    n = 5
    s1 = "01011"
    s2 = "11001"
    print(countWays(s1, s2, n))
