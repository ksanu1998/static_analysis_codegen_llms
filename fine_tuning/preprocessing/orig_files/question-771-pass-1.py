def makeSumX(arr, X, S, i):
    if i == len(arr):
        return S == X
    a = str(arr[i])
    l = int(a[:-1])
    r = int(a[1:])
    x = makeSumX(arr, X, S + l, i + 1)
    y = makeSumX(arr, X, S + r, i + 1)
    return x | y


def Check(arr, X):
    if (makeSumX(arr, X, 0, 0)):
    print("Yes")
    else:
    print("No")


arr = [545, 433, 654, 23]
X = 134
Check(arr, X)
