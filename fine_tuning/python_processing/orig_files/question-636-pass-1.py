def maxRepeating(str):
    n = len(str)
    count = 0
    res = str[0]
    cur_count = 1
    for i in range(n):
        if (i < n - 1 and str[i] == str[i + 1]):
            cur_count += 1
        else:
            if cur_count > count:
                count = cur_count
                res = str[i]
            cur_count = 1
    return res


if __name__ == "__main__":
    str = "aaaabbaaccde"
    print(maxRepeating(str))
