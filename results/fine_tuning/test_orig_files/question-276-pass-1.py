import math



def countNumbers(N):
    count = 0
    for i in range(1, N):
        root = math.sqrt(i)
        if root == int(root):
            count += 1
    return count
