def hasEqualBlockFrequency(N):
    binary_string = bin(N)[2:]
    zero_count = binary_string.count('0')
    one_count = binary_string.count('1')
    return zero_count == one_count
