def are_distinct(strr, i, j):
    return len(set(strr[i:j+1])) == j - i + 1
