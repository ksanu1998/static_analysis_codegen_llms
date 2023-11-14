import math as mt


def check_sub(sub, s):
    if len(sub) == 0:
        return s == 0
    for i in range(len(sub)):
        if s % sub[i] == 0:
            return check_sub(sub[i+1:], s // sub[i])
    return False
