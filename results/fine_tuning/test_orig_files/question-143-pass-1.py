def find_numbers(N):

def find_numbers(N):
    numbers = []
    for i in range(1, N):
        if i % 3 == 0:
            numbers.append(i)
    return numbers
