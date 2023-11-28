MAX_CHARS = 256


def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False
    marked = [False] * MAX_CHARS
    map = [-1] * MAX_CHARS
    for i in xrange(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])]:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True


print areIsomorphic("aab", "xxy")
print areIsomorphic("aab", "xyz")
