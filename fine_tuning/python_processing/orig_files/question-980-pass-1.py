def countWays(n):
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    if (i + j + k + l == n):
                        counter += 1
    return counter


if __name__ == "__main__":
    n = 8
    print(countWays(n))
