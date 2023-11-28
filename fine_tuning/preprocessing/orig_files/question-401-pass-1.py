def maxSumBitonicSubArr(arr, n):
    max_sum = -10 ** 9
    i = 0
    while (i < n):
        j = i
        while (j + 1 < n and arr[j] < arr[j + 1]):
            j += 1
        while (i < j and arr[i] <= 0):
            i += 1
        k = j
        while (k + 1 < n and arr[k] > arr[k + 1]):
            k += 1
        last = k
        while (k > j and arr[k] <= 0):
            k -= 1
        nn = arr[i:j + 1]
        sum_inc = sum(nn)
        nn = arr[j:k + 1]
        sum_dec = sum(nn)
        sum_all = sum_inc + sum_dec - arr[j]
        max_sum = max([max_sum, sum_inc, sum_dec, sum_all])
        i = max(last, i + 1)
    return max_sum


arr = [5, 3, 9, 2, 7, 6, 4]
n = len(arr)
print("Maximum Sum = ", maxSumBitonicSubArr(arr, n))
arr2 = [1, 2, 3, 4, 5]
n2 = len(arr2)
print("Maximum Sum = ", maxSumBitonicSubArr(arr2, n2))
arr3 = [5, 4, 3, 2, 1]
n3 = len(arr3)
print("Maximum Sum = ", maxSumBitonicSubArr(arr3, n3))
arr4 = [5, 5, 5, 5]
n4 = len(arr4)
print("Maximum Sum = ", maxSumBitonicSubArr(arr4, n4))
arr5 = [-1, 0, 1, 2, 3, 1, 0, -1, -10]
n5 = len(arr5)
print("Maximum Sum = ", maxSumBitonicSubArr(arr5, n5))
arr6 = [-1, 0, 1, 2, 0, -1, -2, 0, 1, 3]
n6 = len(arr6)
print("Maximum Sum = ", maxSumBitonicSubArr(arr6, n6))
