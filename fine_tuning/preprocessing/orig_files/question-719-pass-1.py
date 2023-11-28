def center_nonadecagon_num(n):
    return (19 * n * n - 19 * n + 2) // 2


if __name__ == '__main__':
    n = 2
    print(n, "nd centered nonadecagonal " +
          "number : ", center_nonadecagon_num(n))
    n = 7
    print(n, "nd centered nonadecagonal " +
          "number : ", center_nonadecagon_num(n))
