def findLength(str1, str2):
    # Initialize variables
    max_length = 0
    length = 0

    # Loop through each character in str1
    for i in range(len(str1)):
        # Check if the character is present in str2
        if str2.find(str1[i])!= -1:
            # Increment the length of the substring
            length += 1
        else:
            # If the character is not present, check if the length is greater than the max length
            if length > max_length:
                max_length = length
            # Reset the length of the substring
            length = 0

    # If the length of the last substring is greater than the max length, update the max length
    if length > max_length:
        max_length = length

    return max_length
