def Max_Sum(arr1, arr2, n):
    max_sum = 0
    for i in range(n):
        for j in range(n):
            current_sum = arr1[i] + arr2[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
