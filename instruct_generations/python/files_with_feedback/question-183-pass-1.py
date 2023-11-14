def create_array(N, even, odd):
    arr = []
    for i in range(N):
        if i % 2 == 0:
            arr.append(even)
        else:
            arr.append(odd)
    return arr
