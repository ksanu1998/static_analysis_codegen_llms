def decideWinner(a, n):
    diff = abs(a - n)
    if diff == 0:
        return "tie"
    elif diff < a:
        return "n"
    else:
        return "a"
