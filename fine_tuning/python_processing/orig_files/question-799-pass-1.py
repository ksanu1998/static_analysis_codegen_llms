def sortStack(input):
    tmpStack = []
    while (len(input) > 0):
        tmp = input[-1]
        input .pop()
        while (len(tmpStack) > 0 and tmpStack[-1] < tmp):
            input .append(tmpStack[-1])
            tmpStack .pop()
        tmpStack .append(tmp)
    return tmpStack


def sortArrayUsingStacks(arr, n):
    input = []
    i = 0
    while (i < n):
        input .append(arr[i])
        i = i + 1
    tmpStack = sortStack(input)
    i = 0
    while (i < n):
        arr[i] = tmpStack[-1]
        tmpStack .pop()
        i = i + 1
    return arr


arr = [10, 5, 15, 45]
n = len(arr)
arr = sortArrayUsingStacks(arr, n)
i = 0
while (i < n):
    print(arr[i], end=" ")
    i = i + 1
