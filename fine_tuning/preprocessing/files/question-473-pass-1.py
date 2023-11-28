def findSubsequence(S, ch):
    # Initialize variables
    max_len = 0
    start = 0
    end = 0

    # Iterate over the string
    for i in range(len(S)):
        # Check if the current character is the same as the previous character
        if S[i] == ch:
            # Increment the end index
            end += 1
        else:
            # Check if the subsequence is longer than the current longest subsequence
            if end - start > max_len:
                max_len = end - start
                start = i + 1
            else:
                start = i + 1

    # Check if the last subsequence is the longest
    if end - start > max_len:
        max_len = end - start

    return max_len
