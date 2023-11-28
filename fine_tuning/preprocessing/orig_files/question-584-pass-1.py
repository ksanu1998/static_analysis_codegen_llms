def newString(s):
    l = len(s)
    freq = [0] * (26)
    for i in range(0, l):
        freq[ord(s[i]) - ord('a')] += 1
    ans = ""
    for i in range(0, 26):
        for j in range(0, freq[i]):
            ans += chr(97 + i)
    return ans


if __name__ == "__main__":
    s = "aabab"
    print(newString(s))
