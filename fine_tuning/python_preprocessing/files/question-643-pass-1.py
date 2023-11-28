def countkDist(str1, k):
    count = 0
    for i in range(len(str1) - k + 1):
        if len(set(str1[i:i+k])) == k:
            count += 1
    return count
