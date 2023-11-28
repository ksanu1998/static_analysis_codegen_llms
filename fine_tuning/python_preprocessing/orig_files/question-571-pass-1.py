def maximum_one(s, n):
    cnt_one = 0
    cnt, max_cnt = 0, 0
    for i in range(n):
        if (s[i] == '1'):
            cnt_one += 1
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    left = [0] * n
    right = [0] * n
    if (s[0] == '1'):
        left[0] = 1
    else:
        left[0] = 0
    if (s[n - 1] == '1'):
        right[n - 1] = 1
    else:
        right[n - 1] = 0
    for i in range(1, n):
        if (s[i] == '1'):
            left[i] = left[i - 1] + 1
        else:
            left[i] = 0
    for i in range(n - 2, -1, -1):
        if (s[i] == '1'):
            right[i] = right[i + 1] + 1
        else:
            right[i] = 0
    for i in range(1, n - 1):
        if (s[i] == '0'):
            sum = left[i - 1] + right[i + 1]
            if (sum < cnt_one):
                max_cnt = max(max_cnt, sum + 1)
            else:
                max_cnt = max(max_cnt, sum)
    return max_cnt


if __name__ == "__main__":
    s = "111011101"
    print(maximum_one(s, len(s)))
