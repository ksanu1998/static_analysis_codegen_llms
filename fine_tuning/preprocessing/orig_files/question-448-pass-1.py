def restore(arr, N):
    result = []
    count1 = 1
    s = set([])
    for i in range(N):
        s .add(arr[i])
        if (len(s) == count1):
            result .append(arr[i])
            count1 += 1
    return result


def print_result(result):
    for i in range(len(result)):
        print(result[i], end=" ")


if __name__ == "__main__":
    arr = [1, 13, 1, 24, 13, 24, 2, 2]
    N = len(arr)
    print_result(restore(arr, N))
