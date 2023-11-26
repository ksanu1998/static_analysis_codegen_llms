MAX = 40
dp = [[-1 for i in range(9 * MAX + 1)]for i in range(MAX)]


def countGroups(position, previous_sum, length, num):
    if position == length:
        return 1
    if dp[position][previous_sum]!= -1:
        return dp[position][previous_sum]
    count = 0
    for i in range(previous_sum + 1, 10):
        if num[position] == i:
            count += countGroups(position + 1, i, length, num)
    dp[position][previous_sum] = count
    return count
