def center_pentadecagonal_num(n):
    return (15 * n * n - 15 * n + 2) // 2


if __name__ == '__main__':
    n = 3
    print(n, "rd number : ", center_pentadecagonal_num(n))
    n = 10
    print(n, "th number : ", center_pentadecagonal_num(n))
