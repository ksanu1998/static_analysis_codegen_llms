def solve(ang, n):
    if (n == 1):
        print(ang)
        return
    solve(ang, n - 1)
    ang = (ang + 1) % 360
    solve(ang, n - 1)


if __name__ == "__main__":
    n = 3
    solve(0, n)
