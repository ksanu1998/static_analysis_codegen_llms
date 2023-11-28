def count_carry(a, b):
    carry = 0
    while a > 0 or b > 0:
        sum = a % 10 + b % 10 + carry
        if sum > 9:
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    return carry
