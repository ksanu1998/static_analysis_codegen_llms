def findMaximumNum(st, n, k):

def findMaximumNum(st, n, k):
    # Initialize a list to store the largest number
    largest_num = []
    # Loop through each digit in the string
    for i in range(n):
        # Get the current digit
        digit = st[i]
        # If the digit is not a zero, add it to the list
        if digit!= "0":
            largest_num.append(digit)
    # If the list is empty, return 0
    if len(largest_num) == 0:
        return 0
    # If the list has only one element, return the element
    if len(largest_num) == 1:
        return int(largest_num[0])
    # Sort the list in descending order
    largest_num.sort(reverse=True)
    # Get the first K elements of the list
    largest_num = largest_num[:k]
    # Join the elements of the list into a string
    largest_num = "".join(largest_num)
    # Return the largest number
    return int(largest_num)
