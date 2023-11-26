def countPairs(str1):
    count = 0
    for i in range(len(str1) - 1):
        if str1[i] == str1[i+1]:
            count += 1
    return count
