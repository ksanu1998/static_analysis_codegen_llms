def sumArr(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print(sumArr(arr, n))
