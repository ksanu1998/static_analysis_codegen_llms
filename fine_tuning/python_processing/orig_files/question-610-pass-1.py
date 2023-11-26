MAX_CHAR = 256


def isPresent(s, q):
    freq = [0] * MAX_CHAR
    for i in range(0, len(s)):
        freq[ord(s[i])] += 1
    for i in range(0, len(q)):
        freq[ord(q[i])] -= 1
        if (freq[ord(q[i])] < 0):
            return False
    return True


s = "abctd"
q = "cat"
if (isPresent(s, q)):
    print("Yes")
else:
    print("No")
