def allOddDigits(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if int(str_n[i]) % 2 == 0:
            return False
    return True
