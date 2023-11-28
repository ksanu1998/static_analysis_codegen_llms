def reversedigit(num):
    rev = 0
    while (num > 0):
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev


def isIccanobif(num):
    if (num == 0):
        return 1
    if (num == 1):
        return 0
    if (isIccanobif(reversedigit(num)) == 1):
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = 5
    print("First", n, "Iccanobif Numbers are")
    for (i = 1; i <= n; i++)
        if (isIccanobif(i) == 1):
            print(i)
