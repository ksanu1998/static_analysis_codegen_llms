def findNthOccur(string, ch, N):
    occur = 0
    for i in range(len(string)):
        if (string[i] == ch):
            occur += 1
        if (occur == N):
            return i
    return -1


if __name__ == "__main__":
    string = "geeks"
    ch = 'e'
    N = 2
    print(findNthOccur(string, ch, N))
