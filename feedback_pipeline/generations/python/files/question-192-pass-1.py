def decideWinner(a, n):
    # Calculate the absolute difference of sum for both numbers
    diff = abs(a - n)
    # Return the number with the minimum absolute difference
    if diff == 0:
        return "tie"
    elif diff < a:
        return "n"
    else:
        return "a"