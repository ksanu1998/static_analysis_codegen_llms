dp = [0] * 1024


def get_binary(u):
    binary = []
    while u > 0:
        binary.append(u % 2)
        u //= 2
    return binary[::-1]
