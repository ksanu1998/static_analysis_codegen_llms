def CreateArray(N, even, odd):

def create_array(n, even, odd):
    arr = []
    for i in range(n):
        if i % 2 == 0:
            arr.append(even)
        else:
            arr.append(odd)
    return arr
