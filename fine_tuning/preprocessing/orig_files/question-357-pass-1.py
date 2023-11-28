def get_max_splits(num_string):
    count = 0
    running_sum = 0
    for i in range(len(num_string)):
        current_num = int(num_string[i])
        running_sum += current_num
        if current_num % 3 == 0 or (running_sum != 0 and running_sum % 3 == 0):
            count += 1
            running_sum = 0
    return count


print get_max_splits("12345")
