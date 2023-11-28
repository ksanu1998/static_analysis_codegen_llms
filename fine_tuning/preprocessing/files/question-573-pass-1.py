def maxFreq(s, a, b):
    # Initialize variables
    max_count = 0
    start_index = 0
    end_index = 0

    # Loop through the string
    for i in range(len(s)):
        # Check if the current character is 'a'
        if s[i] == a:
            # Increment the count of 'a'
            count_a += 1
        # Check if the current character is 'b'
        elif s[i] == b:
            # Increment the count of 'b'
            count_b += 1

        # Check if the current character is 'a' or 'b'
        if s[i] == a or s[i] == b:
            # Check if the count of 'a' or 'b' is greater than the max count
            if count_a > max_count or count_b > max_count:
                # Update the max count and the indices of the substring
                max_count = max(count_a, count_b)
                start_index = i - count_a + 1
                end_index = i + 1

    # Return the substring
    return s[start_index:end_index]
