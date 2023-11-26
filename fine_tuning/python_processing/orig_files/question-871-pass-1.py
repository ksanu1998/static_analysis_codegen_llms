def printCubeFree(n):
    cubFree = [1] * (n + 1)
    i = 2
    while (i * i * i <= n):
        if (cubFree[i] == 1):
            multiple = 1
            while (i * i * i * multiple <= n):
                cubFree[i * i * i * multiple] = 0
                multiple += 1
        i += 1
    for i in range(2, n + 1):
        if (cubFree[i] == 1):
            print(i, end=" ")


if __name__ == "__main__":
    printCubeFree(20)
