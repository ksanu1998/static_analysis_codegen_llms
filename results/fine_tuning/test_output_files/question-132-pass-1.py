def digitSum(n):
    sum = 0
    while (n > 0):
        sum += (n % 10)
        n //= 10
    if (sum == 0):
        return 1
    if (sum % 2 == 0):
        return 1
    return 0


if __name__ == "__main__":
    n = 121
    if (digitSum(n)):
        print("Yes")
    else:
        print("No")
