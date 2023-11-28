def removeConsecutiveSame(my_list):
    return [x for i, x in enumerate(my_list) if x!= my_list[i-1]]
