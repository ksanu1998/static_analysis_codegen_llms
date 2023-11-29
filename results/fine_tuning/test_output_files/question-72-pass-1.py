def Centered_Pentadecagonal_num(n):
    if (n == 1):
        return 1
    else:
        c = Centered_Pentadecagonal_num(n - 1)
        return (c * (c + 1) / 2) + (n * (n + 1) / 2)


if __name__ == "__main__":
    n = 10
    print(Centered_Pentadecagonal_num(n))
