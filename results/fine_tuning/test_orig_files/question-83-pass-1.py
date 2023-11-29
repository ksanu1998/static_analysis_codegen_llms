def count_pairs(x):

def count_pairs(x):
    count = 0
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if (i | j) == x:
                count += 1
    return count
