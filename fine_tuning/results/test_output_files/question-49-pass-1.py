def CountPairs(arr, n):
    count = 0
    for (i = 0; i < n; i++)
        if (arr[i] % 2 == 0)
            count++;
    for (i = 1; i < n; i++)
        for (j = 0; j < i; j++)
            if (arr[i] % 2 == 0 && arr[j] % 2 == 0)
                count++;
    return count;


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print(CountPairs(arr, n))
