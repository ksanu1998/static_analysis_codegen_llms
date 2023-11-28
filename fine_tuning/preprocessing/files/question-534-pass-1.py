MAX = 26


def minOperations(str, len):
    count = 0
    for i in range(len):
        if str[i] == 'a':
            count += 1
    return count
