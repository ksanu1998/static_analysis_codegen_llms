def check(k, d0, d1):
    s = ((2 * (d0 + d1)) %
         10 + (4 * (d0 + d1)) %
         10 + (8 * (d0 + d1)) %
         10 + (6 * (d0 + d1)) %
         10)
    a = (k - 3) % 4
    if (a == 0):
        x = 0
    elif (a == 1):
        x = (2 * (d0 + d1)) % 10
    elif (a == 2):
        x = ((2 * (d0 + d1)) % 10 + (4 * (d0 + d1)) % 10)
    elif (a == 3):
        x = ((2 * (d0 + d1)) %
             10 + (4 * (d0 + d1)) %
             10 + (8 * (d0 + d1)) %
             10)
    sum = d0 + d1 + ((k - 3) // 4) * s + x
    if (sum % 3 == 0):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    k = 13
    d0 = 8
    d1 = 1
    print(check(k, d0, d1))
    k = 5
    d0 = 3
    d1 = 4
    print(check(k, d0, d1))
