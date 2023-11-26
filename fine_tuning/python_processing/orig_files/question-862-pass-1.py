def dodecahedral_num(n):
    return n * (3 * n - 1) * (3 * n - 2) // 2


n = 5
print("%sth Dodecahedral number :" % n, dodecahedral_num(n))
