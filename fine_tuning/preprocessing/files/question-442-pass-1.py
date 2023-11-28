def lcs(i, j, count):
    if i == len(s1) or j == len(s2):
        return count
    if s1[i] == s2[j]:
        return lcs(i + 1, j + 1, count + 1)
    else:
        return max(lcs(i + 1, j, count), lcs(i, j + 1, count))
