MAX = 1000
arr = []


def ulam():
    for i in range(1, MAX):
        if (i == 1):
            arr.append(1)
        else:
            if (i % 2 == 0):
                arr.append(0)
            else:
                arr.append(1)


if __name__ == "__main__":
    ulam()
    print(arr)
