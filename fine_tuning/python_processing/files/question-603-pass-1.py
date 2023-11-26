import math


def count_substr_odd_decimal(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 0 or len(substr) == 1:
                continue
            if substr[0] == '0':
                count += 1
    return count
