def lcm_fun(a, b):
    if (b == 0):
        return a
    return lcm_fun(b, a % b)


def digitLCM(n):
    lcm = 1
    while (n > 0):
        lcm = int((n % 10 * lcm) / lcm_fun(n % 10, lcm))
        if (lcm == 0):
            return 0
        n = int(n / 10)
    return lcm


n = 397
print(digitLCM(n))
