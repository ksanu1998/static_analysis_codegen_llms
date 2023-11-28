def printPowerSet(arr, n):
    _list = []
    for i in range(2 ** n):
        subset = ""
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"
        if subset not in _list and len(subset) > 0:
            _list .append(subset)
    for subset in _list:
        arr = subset .split(' ')
        for string in arr:
            print(string, end=" ")
        print()


if __name__ == '__main__':
    arr = [10, 12, 12]
    n = len(arr)
    printPowerSet(arr, n)
