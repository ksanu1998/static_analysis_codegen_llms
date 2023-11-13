MAX = 1000
arr = []


def ulam(max):
    arr = [True] * (max + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(max ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, max + 1, i):
                arr[j] = False
    return arr