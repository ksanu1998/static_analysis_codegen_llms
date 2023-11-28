def charactersCount(str, n):
    count = 0
    while (n > 0):
        cur = str[0]
        ind = 0
        for j in range(1, n):
            if (str[j] < cur):
                cur = str[j]
                ind = j
        str = str[0:ind] + str[ind + 1:]
        n -= 1
        count += ind + 1
    print(count)


if __name__ == '__main__':
    str = "aabbc"
    n = 5
    charactersCount(str, n)
