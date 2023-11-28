dp = [[0 for i in range(1000)]for i in range(1000)]


def create_palindrome(input, is_odd):
    if input == 0:
        return 0
    if is_odd:
        return 1
    else:
        return 2
