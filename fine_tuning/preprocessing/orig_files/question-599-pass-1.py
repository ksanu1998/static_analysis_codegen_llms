MAX = 256


def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


def countPalinPermutations(str):
    global MAX
    n = len(str)
    freq = [0] * MAX
    for i in range(0, n):
        freq[ord(str[i])] = freq[ord(str[i])] + 1
    res = fact(int(n / 2))
    oddFreq = False
    for i in range(0, MAX):
        half = int(freq[i] / 2)
        if (freq[i] % 2 != 0):
            if (oddFreq):
                return 0
            oddFreq = True
        res = int(res / fact(half))
    return res


str = "gffg"
print(countPalinPermutations(str))
