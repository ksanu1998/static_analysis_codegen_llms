def hendecagonal_num(n):
    return (9 * n * n - 7 * n) // 2


if __name__ == '__main__':
    n = 3
    print(n, "rd Hendecagonal number : ", hendecagonal_num(n))
    n = 10
    print(n, "th Hendecagonal number : ", hendecagonal_num(n))
