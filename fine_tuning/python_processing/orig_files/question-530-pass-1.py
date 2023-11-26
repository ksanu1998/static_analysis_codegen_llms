MAX = 26


def compressString(s, n):
    freq = [0] * MAX
    for i in range(n):
        freq[ord(s[i]) - ord('a')] += 1
    for i in range(MAX):
        if (freq[i] == 0):
            continue
        print((chr)(i + ord('a')), freq[i], end=" ")


if __name__ == "__main__":
    s = "geeksforgeeks"
    n = len(s)
    compressString(s, n)
