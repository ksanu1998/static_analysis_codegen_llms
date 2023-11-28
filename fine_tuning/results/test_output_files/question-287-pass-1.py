def Sum_upto_nth_Term(n):
    s = 0
    for i in range(1, n):
        s = s + (2 * i - 1) * (4 * i - 3)
    print(s)


if __name__ == "__main__":
    Sum_upto_nth_Term(10)
