def Centered_Dodecagonal_num(n):
    if (n == 1):
        return 1
    else:
        return (n * (n + 1) / 2)


if __name__ == "__main__":
    n = 5
    print(Centered_Dodecagonal_num(n))
