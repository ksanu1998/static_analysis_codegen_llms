def lenOfLongestGP(sett, n):
    # Initialize variables
    max_len = 0
    curr_len = 1
    curr_term = sett[0]

    # Iterate through the terms of the sequence
    for i in range(1, n):
        # Check if the current term is part of the geometric progression
        if sett[i] == curr_term * sett[i-1]:
            curr_len += 1
        else:
            # If it's not part of the GP, check if it's the longest GP so far
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
            curr_term = sett[i]

    # Check if the last term is part of the GP
    if curr_len > max_len:
        max_len = curr_len

    return max_len
