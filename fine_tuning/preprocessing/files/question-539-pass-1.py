def get_count(str1, n):
    count = 0
    for i in range(n - 2):
        if str1[i]!= str1[i + 1] and str1[i + 1]!= str1[i + 2]:
            count += 1
    return count
