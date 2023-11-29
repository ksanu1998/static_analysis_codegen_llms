def find_numbers(N):
    numbers = []
    for i in range(1, N):
        if i % 2 == 0:
            continue
        for j in range(i, 3 * i):
            if j % 3 == 0:
                numbers.append(j)
                if len(numbers) == 3:
                    return numbers
    return None