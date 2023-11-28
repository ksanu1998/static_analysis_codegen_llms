def powers_of_two(x):
    result = []
    power = 1
    while power <= x:
        result.append(power)
        power *= 2
    return result[::-1]
