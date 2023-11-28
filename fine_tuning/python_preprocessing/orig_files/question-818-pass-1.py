def removeConsecutiveSame(v):
    n = len(v)
    i = 0
    while (i < n - 1):
        if ((i + 1) < len(v)) and (v[i] == v[i + 1]):
            v = v[:i]
            v = v[:i]
            if (i > 0):
                i -= 1
            n = n - 2
        else:
            i += 1
    return len(v[:i - 1])


if __name__ == '__main__':
    v = ["tom", "jerry", "jerry", "tom"]
    print(removeConsecutiveSame(v))
