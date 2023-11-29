def center_heptagonal_num(n):

def center_heptagonal_num(n):
    # Initialize the sum to 0
    sum = 0
    # Loop through the first N centered heptagonal numbers
    for i in range(1, n+1):
        # Calculate the current centered heptagonal number
        num = (i**2 + i) // 2
        # Add it to the sum
        sum += num
    # Return the sum
    return sum
