def count_acronym(n, arr):
    count = 0
    for i in range(n):
        word = arr[i]
        if len(word) > 1 and word[0] == word[0].upper():
            count += 1
    return count
