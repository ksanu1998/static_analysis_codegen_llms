def count(arr, N, K):
    count = 0
    for (i = 0; i < N; i++)
        if (arr[i] == K)
            count++;
    return count;


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = len(arr)
    K = 5
    print(count(arr, N, K))
