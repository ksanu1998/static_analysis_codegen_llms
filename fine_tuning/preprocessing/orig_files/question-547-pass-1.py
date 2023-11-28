def find_digit(s, n):
    first_digit = -1
    for i in range(n - 1, -1, -1):
        if s[i] < '0' or s[i] > '9':
            first_digit = i
            break
    first_digit += 1
    s_len = first_digit
    num = 0
    pw = 1
    i = n - 1
    while i >= 0:
        if s[i] >= '0' and s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num + (pw * digit)
            if num >= s_len:
                return -1
            pw = pw * 10
        i -= 1
    num = num * 10
    req = s_len - num
    if req > 9 or req < 0:
        return -1
    return req


if __name__ == "__main__":
    s = "abcd0"
    n = len(s)
    print(find_digit(s, n))
