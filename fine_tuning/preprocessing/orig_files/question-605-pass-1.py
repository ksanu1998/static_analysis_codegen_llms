def canMakeStr2(s1, s2):
    count = {s1[i]: 0 for i in range(len(s1))}
    for i in range(len(s1)):
        count[s1[i]] += 1
    for i in range(len(s2)):
        if (count .get(s2[i]) is None or count[s2[i]] == 0):
            return False
        count[s2[i]] -= 1
    return True


s1 = "geekforgeeks"
s2 = "for"
if canMakeStr2(s1, s2):
    print("Yes")
else:
    print("No")
