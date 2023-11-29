def pairwiseDifference(arr, n):
    diff = 0
    for (i = 0; i < n - 1; i++)
        diff += abs(arr[i] - arr[i + 1]);
    print(diff);


arr = [1, 2, 3, 4, 5]
n = len(arr)
pairwiseDifference(arr, n)

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
pairwiseDifference(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
pairwiseDifference(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
pairwiseDifference(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
pairwiseDifference(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
pairwiseDifference(arr, n)
