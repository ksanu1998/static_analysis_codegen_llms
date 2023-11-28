def checkRecursive(num, rem_num, next_int, n, ans=0):
    if num == 0:
        return ans
    if rem_num == 0:
        return -1
    if next_int > rem_num:
        return -1
    if num - next_int < 0:
        return -1
    if num - next_int == 0:
        return ans + 1
    return checkRecursive(num - next_int, rem_num, next_int, n, ans + 1)
