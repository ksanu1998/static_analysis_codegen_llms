def checkLuhn(cardNo):
    digits = [int(digit) for digit in cardNo]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum([int(digit) for digit in str(digit*2)])
    return total % 10 == 0
