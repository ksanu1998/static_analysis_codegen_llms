def findAandB(n, k):

def findAandB(n, k):
    for i in range(1, n):
        if i % 10!= k and n - i % 10!= k:
            return (i, n - i)
    return (None, None)
