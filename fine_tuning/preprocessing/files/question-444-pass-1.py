def countPalindrome(S):
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            substring = S[i:j+1]
            if substring == substring[::-1]:
                count += 1
    return count
