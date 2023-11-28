MOD = 1000000007


def number_of_ways(arr, n, k):
    if n == k:
        return 1
    if k == 0:
        return 0
    if arr[n-1] > k:
        return number_of_ways(arr, n-1, k)
    else:
        return (number_of_ways(arr, n-1, k) + number_of_ways(arr, n-1, k-arr[n-1])) % MOD
