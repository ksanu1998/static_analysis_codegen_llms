def center_octadecagon_num(n):

def center_octadecagon_num(n):
    # Initialize a list to store the first N centered octadecagonal numbers
    centered_octadecagon_nums = []

    # Initialize a variable to store the current number
    current_num = 1

    # Loop through the first N numbers
    for i in range(n):
        # Add the current number to the list
        centered_octadecagon_nums.append(current_num)

        # Increment the current number by 1
        current_num += 1

    # Return the sum of the list
    return sum(centered_octadecagon_nums)
