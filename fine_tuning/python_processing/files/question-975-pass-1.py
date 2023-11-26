def countEvenSum(arr, n):
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum % 2 == 0:
                count += 1
    return count
