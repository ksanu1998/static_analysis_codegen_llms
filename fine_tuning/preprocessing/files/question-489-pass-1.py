def longestSubstring(s):
    # Initialize variables
    max_len = 0
    start = 0
    end = 0

    # Iterate over the string
    for i in range(len(s)):
        # Check if the character is a palindrome
        if s[i] == s[i]:
            # If the character is a palindrome, update the start and end indices
            start = i
            end = i + 1

            # Iterate over the remaining characters
            for j in range(i + 1, len(s)):
                # Check if the character is a palindrome
                if s[j] == s[j]:
                    # If the character is a palindrome, update the end index
                    end = j + 1

                    # Check if the substring is the longest
                    if end - start > max_len:
                        max_len = end - start

    # Return the longest substring
    return s[start:end]
