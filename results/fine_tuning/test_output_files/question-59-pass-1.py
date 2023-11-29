from math import pow, ceil


def solve(n):
    for (i, j) in zip(range(1, ceil(pow(n, 0.25))), range(ceil(pow(n, 0.25)), 0, -1)):
        if (pow(i, 4) - pow(j, 4) == n):
            print(i, j)
            break


if __name__ == "__main__":
    solve(16)
