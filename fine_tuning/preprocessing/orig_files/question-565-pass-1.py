import math as mt


def findPermutation(string, k):
    has = [False for i in range(26)]
    cnt = 0
    for i in range(len(string)):
        if (has[ord(string[i]) - ord('a')] == False):
            cnt += 1
            has[ord(string[i]) - ord('a')] = True
    ans = 1
    for i in range(2, cnt + 1):
        ans *= i
    for i in range(cnt - k, 1, -1):
        ans //= i
    return ans


string = "geeksforgeeks"
k = 4
print(findPermutation(string, k))
