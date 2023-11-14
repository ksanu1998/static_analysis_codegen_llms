MAX = 1000
arr = []


def ulam():
    arr = [True] * (MAX + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(MAX ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, MAX + 1, i):
                arr[j] = False
    return arr
