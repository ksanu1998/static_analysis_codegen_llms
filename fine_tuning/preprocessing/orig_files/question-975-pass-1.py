def countEvenSum(arr, n):
    res = 0
    s = 0
    for i in reversed(range(n)):
        if arr[i] % 2 == 1:
            s = n - i - 1 - s
        else:
            s = s + 1
        res = res + s
    return res


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 1]
    n = len(arr)
    print("The Number of Subarrays with even" " sum is", countEvenSum(arr, n))
