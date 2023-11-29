def find_distinct_odd_summ(n, k):
    result = []
    num = 1
    sum = 0
    while len(result) < k:
        if sum < n:
            result.append(num)
            sum += num
            num += 2
        else:
            result.pop()
            sum -= num
            num -= 2
    return result
