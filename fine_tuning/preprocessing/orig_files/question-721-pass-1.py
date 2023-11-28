def cen_octagonalnum(n):
    return (4 * n * n - 4 * n + 1)


if __name__ == '__main__':
    n = 6
    print(n, "th Centered", "octagonal number: ", cen_octagonalnum(n))
    n = 11
    print(n, "th Centered", "octagonal number: ", cen_octagonalnum(n))
