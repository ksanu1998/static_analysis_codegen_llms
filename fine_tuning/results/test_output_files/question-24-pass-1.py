def countRepeatingDigits(N):
    count = 0
    for i in range(1, 10):
        if (N // i) % 10 == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    N = 123456
    countRepeatingDigits(N)
