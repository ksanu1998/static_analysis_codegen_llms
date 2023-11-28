MOD = 1000000007


def powerLL(x, n):
    result = 1
    while (n):
        if (n & 1):
            result = result * x % MOD
        n = int(n / 2)
        x = x * x % MOD
    return result


def powerStrings(sa, sb):
    a = 0
    b = 0
    for i in range(len(sa)):
        a = (a * 10 + (ord(sa[i]) - ord('0'))) % MOD
    for i in range(len(sb)):
        b = (b * 10 + (ord(sb[i]) - ord('0'))) % (MOD - 1)
    return powerLL(a, b)


sa = "2"
sb = "3"
print(powerStrings(sa, sb))
