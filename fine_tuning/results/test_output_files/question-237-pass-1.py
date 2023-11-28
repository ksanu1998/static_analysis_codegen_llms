def candies(n, k):
    if (n < k):
        print("No Solution")
        return
    n = n // k
    i = 1
    while (i <= n):
        if (n % i == 0):
            print(i)
            i = 1
        else:
            i = i + 1


if __name__ == "__main__":
    n = 10
    k = 3
    candies(n, k)
