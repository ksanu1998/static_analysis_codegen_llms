def rearrangeString(s1, s2):
    cnt = [0] * 26
    for i in range(len(s2)):
        cnt[ord(s2[i]) - ord('a')] += 1
    unique = 0
    for i in range(26):
        if (cnt[i] != 0):
            unique += 1
    if (unique == 1):
        count_in_s2 = len(s2)
        count_in_s1 = 0
        for i in range(len(s1)):
            if (s1[i] == s2[0]):
                count_in_s1 += 1
        if (count_in_s1 < count_in_s2):
            print(s1, end="")
            return
        print(-1, end="")
    else:
        inc = 1
        for i in range(len(s2) - 1):
            if (s2[i] > s2[i + 1]):
                inc = 0
        if (inc == 1):
            s1 = sorted(s1)[::-1]
            print("".join(s1), end="")
        else:
            s1 = sorted(s1)
            print("".join(s1), end="")


if __name__ == '__main__':
    s1, s2 = "abcd", "ab"
    rearrangeString(s1, s2)
