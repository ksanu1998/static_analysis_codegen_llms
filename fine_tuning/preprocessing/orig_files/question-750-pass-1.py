def Avgdifference(arr, N, K):
    sum = 0
    for i in range(K):
        sum += arr[i]
    min = sum
    max = sum
    for i in range(K, N - K + 2, 1):
        sum += arr[i] - arr[i - K]
        if (min > sum):
            min = sum
        if (max < sum):
            max = sum
    return (max - min) / K


if __name__ == '__main__':
    arr = [3, 8, 9, 15]
    N = len(arr)
    K = 2
    print(Avgdifference(arr, N, K))
