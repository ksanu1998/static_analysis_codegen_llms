def count(arr, low, high, x):
    if ((low > high) or (low == high and arr[low] != x)):
        return 0
    if (low == high and arr[low] == x):
        return 1
    return count(arr, low, (low + high) // 2, x) + \
        count(arr, 1 + (low + high) // 2, high, x)


if __name__ == '__main__':
    arr = [30, 1, 42, 5, 56, 3, 56, 9]
    n = len(arr)
    x = 56
    print(count(arr, 0, n - 1, x))
