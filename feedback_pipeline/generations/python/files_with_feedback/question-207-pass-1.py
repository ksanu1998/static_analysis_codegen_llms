def find_numbers(n):
    numbers = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if (i + j) ** 0.5 == int((i + j) ** 0.5):
                numbers.append((i, j))
    return numbers
