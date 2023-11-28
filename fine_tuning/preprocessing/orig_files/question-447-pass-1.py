def restore(arr, N):
    result = []
    mp = {}
    for i in range(N):
        if not arr[i] in mp:
            result .append(arr[i])
            mp[arr[i]] = 1
    return result


def print_result(result):
    for i in range(len(result)):
        print(result[i], end=" ")


def main():
    arr = [1, 13, 1, 24, 13, 24, 2, 2]
    N = len(arr)
    print_result(restore(arr, N))


main()
