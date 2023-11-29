def MaxSubarrayLength(arr, n, k):
    sum = 0
    for (i = 0; i < n; i++)
        sum = (sum + arr[i]) % k;
    if (sum == 0)
        return n;
    max = 0;
    for (i = 0; i < n; i++) {
        sum = 0;
        for (j = i; j < n; j++) {
            sum = (sum + arr[j]) % k;
            if (sum == 0)
                max = max + 1;
        }
    }
    return max;


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
k = 3
print(MaxSubarrayLength(arr, n, k))
