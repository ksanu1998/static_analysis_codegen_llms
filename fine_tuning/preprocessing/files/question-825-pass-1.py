def pairWiseConsecutive(s):
    return all(s[i+1] == s[i] + 1 for i in range(len(s) - 1))
