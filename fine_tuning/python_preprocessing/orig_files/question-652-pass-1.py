def areDistinct(strr, i, j):
    visited = [0] * (26)
    for k in range(i, j + 1):
        if (visited[ord(strr[k]) - ord('a')]):
            return False
        visited[ord(strr[k]) - ord('a')] = True
    return True


def longestUniqueSubsttr(strr):
    n = len(strr)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if (areDistinct(strr, i, j)):
                res = max(res, j - i + 1)
    return res


if __name__ == '__main__':
    strr = "geeksforgeeks"
    print("The input is ", strr)
    len = longestUniqueSubsttr(strr)
    print("The length of the longest "
          "non-repeating character substring is ", len)
