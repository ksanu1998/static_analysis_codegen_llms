def countSubStr(str, n, x):
    count = 0
    for i in range(n-x+1):
        if str[i:i+x] == str[i+1:i+x+1]:
            count += 1
    return count
