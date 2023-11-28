def decideWinner(a, n):

def decideWinner(a, n):
    # Calculate the absolute difference of sum for both numbers
    diff = abs(a - n)
    # If the absolute difference is less than or equal to 10, then return "Tie"
    if diff <= 10:
        return "Tie"
    # Otherwise, return the number with the larger absolute difference
    else:
        return "Winner" if diff > 10 else "Loser"
