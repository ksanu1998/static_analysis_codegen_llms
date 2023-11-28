import math



def isDroll(n):
    if n == 1:
        return True
    if n == 2:
        return False
    if n % 2 == 0:
        return isDroll(n // 2)
    else:
        return not isDroll(n // 2)
