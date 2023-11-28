def quadrant(s):

import cmath

def quadrant(s):
    x, y = s.real, s.imag
    if x >= 0 and y >= 0:
        return 1
    elif x < 0 and y >= 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
