def maxPresum(a, b):
    max_sum = 0
    for i in range(len(a)):
        for j in range(len(b)):
            current_sum = a[i] + b[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum