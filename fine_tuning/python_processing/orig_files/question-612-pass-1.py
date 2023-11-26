def calculate(s):
    ans = 6
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            if (i + j + k == l + m + n):
                                c = 0
                                if (i != ord(s[0]) - ord('0')):
                                    c += 1
                                if (j != ord(s[1]) - ord('0')):
                                    c += 1
                                if (k != ord(s[2]) - ord('0')):
                                    c += 1
                                if (l != ord(s[3]) - ord('0')):
                                    c += 1
                                if (m != ord(s[4]) - ord('0')):
                                    c += 1
                                if (n != ord(s[5]) - ord('0')):
                                    c += 1
                                if (c < ans):
                                    ans = c
    return ans


if __name__ == "__main__":
    s = "123456"
    print(calculate(s))
