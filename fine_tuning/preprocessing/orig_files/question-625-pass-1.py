def printAllSubstrings(s, n):
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            print(temp)


s = "Geeky"
printAllSubstrings(s, len(s))
