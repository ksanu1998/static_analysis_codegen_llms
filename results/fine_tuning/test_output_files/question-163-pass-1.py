def convert_To_Len_th_base(n, arr, Len, L):
    if (L == 1):
        for i in range(n):
            print(arr[i], end=" ")
        print("")
        return
    for (i = 0; i < n; i++)
        convert_To_Len_th_base(n, arr, Len - 1, L - 1)
    for (i = 0; i < n; i++)
        if (i > 0 and arr[i] == arr[i - 1])
            continue
        arr[L - 1] = arr[i]
        convert_To_Len_th_base(n, arr, Len - 1, L - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    convert_To_Len_th_base(n, arr, n, 3)
