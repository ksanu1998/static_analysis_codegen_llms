def nth_prime_digits_number(number):
    if number <= 0:
        return 0
    prime_digits = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    nth_prime = prime_digits[number - 1]
    return nth_prime
