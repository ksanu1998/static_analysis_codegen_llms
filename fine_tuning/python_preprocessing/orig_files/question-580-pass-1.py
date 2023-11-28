def printLargestString(s, l, r):
    freq = [0] * 26
    l -= 1
    r -= 1
    for i in range(min(l, r), max(l, r) + 1):
        freq[ord(s[i]) - ord('a')] += 1
    ans = ""
    for i in range(25, -1, -1):
        while (freq[i]):
            ans += chr(ord('a') + i)
            freq[i] -= 1
    return ans


if __name__ == "__main__":
    s = "striver"
    l = 3
    r = 5
    print(printLargestString(s, l, r))
