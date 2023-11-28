def countNumber(n):
    result = 0
    s = []
    for i in range(1, 10):
        if (i <= n):
            s .append(i)
            result += 1
        while len(s) != 0:
            tp = s[-1]
            s .pop()
            for j in range(tp % 10, 10):
                x = tp * 10 + j
                if (x <= n):
                    s .append(x)
                    result += 1
    return result


if __name__ == '__main__':
    n = 15
    print(countNumber(n))
