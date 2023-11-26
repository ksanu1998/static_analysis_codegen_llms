def countSubStr(string, n):
    count = 0
    for i in range(len(string) - n + 1):
        if string[i:i+n] == string[i:i+n]:
            count += 1
    return count
