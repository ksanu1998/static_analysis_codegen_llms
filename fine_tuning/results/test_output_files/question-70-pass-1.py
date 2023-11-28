def Centered_decagonal_num(n):
    if (n == 1):
        return 1
    else:
        ans = Centered_decagonal_num(n - 1)
        ans += (n * (n + 1)) / 2
        return ans


if __name__ == "__main__":
    n = 5
    print(Centered_decagonal_num(n))
