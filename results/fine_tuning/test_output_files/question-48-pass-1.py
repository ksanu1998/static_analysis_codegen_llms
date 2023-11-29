def CountPairs(arr, n):
    cnt = 0
    for (i = 0; i < n; i++)
        if (arr[i] % 2 == 0)
            cnt++;
    if (cnt == 0)
        return 0;
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (arr[i] % 2 == 0 && arr[j] % 2 == 0)
                cnt--;
    return cnt;


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
print(CountPairs(arr, n))
