def countChars(string, n):
    i = 0
    cnt = 0
    while (i < n):
        if (string[i] == '0'):
            i += 1
        else:
            i += 2
        cnt += 1
    return cnt


if __name__ == "__main__":
    string = "11010"
    n = len(string)
    print(countChars(string, n))
