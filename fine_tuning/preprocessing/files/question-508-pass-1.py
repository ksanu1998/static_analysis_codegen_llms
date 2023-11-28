def power(base, pwr):
    if pwr == 0:
        return 1
    else:
        return base * power(base, pwr - 1)
