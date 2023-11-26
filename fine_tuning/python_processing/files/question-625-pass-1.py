def printAllSubstrings(s, n):
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            print(substring)
