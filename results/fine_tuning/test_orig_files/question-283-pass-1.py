def Check_is_possible(l, r, k):

def Check_is_possible(l, r, k):
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            if (i * j) % k == 0:
                return True
    return False
