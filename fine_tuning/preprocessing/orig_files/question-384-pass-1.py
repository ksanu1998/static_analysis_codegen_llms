def gen(n):
    S = [0, 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            S .append(4 * S[int(i / 2)])
        else:
            S .append(4 * S[int(i / 2)] + 1)
    z = S[n]
    return z


def moserDeBruijn(n):
    for i in range(n):
        print(gen(i), end=" ")


n = 15
print("First", n, "terms of ", "Moser-de Brujn Sequence:")
moserDeBruijn(n)
