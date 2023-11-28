def check(s):
    n = len(s)
    for i in range(n - 1):
        if (s[i] > s[i + 1]):
            return True
    return False


if __name__ == '__main__':
    s = "geeksforgeeks"
    if (check(s)):
        print("Yes")
    else:
        print("No")
