def find(n):
    a = 1
    b = 1
    while (a * b < n):
        a += 1
        b += 1
    if (a * b == n):
        print(a, b)
    else:
        print("No such pair exists")


if __name__ == "__main__":
    n = 12
    find(n)
