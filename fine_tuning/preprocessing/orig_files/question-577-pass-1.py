def returnWinner(s, l):
    freq = [0 for i in range(26)]
    for i in range(0, l, 1):
        freq[ord(s[i]) - ord('a')] += 1
    cnt = 0
    for i in range(26):
        if (freq[i] % 2 != 0):
            cnt += 1
    if (cnt == 0 or cnt & 1 == 1):
        return 1
    else:
        return 2


if __name__ == '__main__':
    s = "abaaab"
    l = len(s)
    winner = returnWinner(s, l)
    print("Player-", winner)
