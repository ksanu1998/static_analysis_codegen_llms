def find_all_sequences(N):
    count = 0
    for i in range(N):
        if i % 2 == 0:
            count += 1
    return count
