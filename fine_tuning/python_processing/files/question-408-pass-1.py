def maxSumWithK(a, n, k):
    max_sum = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += a[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum > k:
                break
    return max_sum
