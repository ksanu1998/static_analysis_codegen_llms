def removeRecur(n):
    if n < 10:
        return n
    else:
        return int(str(n)[:-1] + str(n % 10))
