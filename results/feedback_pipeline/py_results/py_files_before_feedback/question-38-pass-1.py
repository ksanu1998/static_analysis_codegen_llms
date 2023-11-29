limit = 10000000
position = [0] * (limit + 1)


def sieve():
    for i in range(2, limit + 1):
        if position[i] == 0:
            for j in range(i * i, limit + 1, i):
                position[j] = 1
    return [i for i in range(2, limit + 1) if position[i] == 0]