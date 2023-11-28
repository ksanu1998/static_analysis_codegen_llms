def solve(n, m, obstacles, rangee):
    val = min(n, m)
    rangee = sorted(rangee)
    c = 1
    for i in range(obstacles - 1, -1, -1):
        rangee[i] = 2 * rangee[i]
        val -= rangee[i]
        if (val <= 0):
            return c
        else:
            c += 1
    if (val > 0):
        return -1


n = 4
m = 5
obstacles = 3
rangee = [1.0, 1.25, 1.15]
print(solve(n, m, obstacles, rangee))
