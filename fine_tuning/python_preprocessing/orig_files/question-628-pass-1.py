def repeat(s, n):
    s1 = s
    for i in range(1, n):
        s += s1
    return s


s = "geeks"
n = 3
print(repeat(s, n))
