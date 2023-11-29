def getResult(n):

def getResult(n):
    # Get the digits of the number at even and odd places
    digits_even = [int(n) % 10]
    digits_odd = [int(n) // 10]

    # Calculate the product of the digits at even and odd places
    product_even = 1
    for digit in digits_even:
        product_even *= digit

    product_odd = 1
    for digit in digits_odd:
        product_odd *= digit

    # Check if the products are equal
    if product_even == product_odd:
        return "Equal"
    else:
        return "Not Equal"
