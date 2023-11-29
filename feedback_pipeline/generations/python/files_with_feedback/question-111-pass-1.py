def quadrant(s):
    if s.real >= 0 and s.imag >= 0:
        return 1
    elif s.real < 0 and s.imag >= 0:
        return 2
    elif s.real < 0 and s.imag < 0:
        return 3
    else:
        return 4
