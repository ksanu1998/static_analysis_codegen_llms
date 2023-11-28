def hexaModK(s, k):
    mp = {}
    for i in range(1, 10):
        mp[chr(i + ord('0'))] = i
    mp['A'] = 10
    mp['B'] = 11
    mp['C'] = 12
    mp['D'] = 13
    mp['E'] = 14
    mp['F'] = 15
    m = int(k)
    base = 1
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        n = mp[s[i]] % m
        ans = (ans + (base % m * n % m) % m) % m
        base = (base % m * 16 % m) % m
    ans = hex(int(ans))[-1].upper()
    print(ans)


if __name__ == "__main__":
    n = "3E8"
    k = "13"
    hexaModK(n, k)
