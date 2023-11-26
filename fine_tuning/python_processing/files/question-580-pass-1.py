def print_largest_string(s, l, r):
    return "".join(sorted(s, key=lambda x: x)[l-1:r])
