def countGroups(position, previous_sum, length, num):
    if position == length:
        return 1
    else:
        count = 0
        for i in range(position, length):
            if num[i] - num[position - 1] <= previous_sum:
                count += countGroups(position + 1, previous_sum, length, num)
        return count
