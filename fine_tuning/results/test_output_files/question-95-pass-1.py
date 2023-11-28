def findUniqueElements(arr, N, K):
    freq = [0] * 100
    for (i = 0; i < N; i++)
        freq[arr[i]] += 1;
    for (i = 0; i < 100; i++)
        if (freq[i] == K)
            return i;


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    N = len(arr)
    K = 2
    print(findUniqueElements(arr, N, K))
