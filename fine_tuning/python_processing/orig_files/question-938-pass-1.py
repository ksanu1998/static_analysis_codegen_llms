def checkJumbled(num):
    if (num / 10 == 0):
        return True
    while (num != 0):
        if (num / 10 == 0):
            return True
        digit1 = num % 10
        digit2 = (num / 10) % 10
        if (abs(digit2 - digit1) > 1):
            return False
        num = num / 10
    return True


num = -1234
if (checkJumbled(abs(num))):
    print "True "
else:
    print "False"
num = -1247
if (checkJumbled(abs(num))):
    print "True "
else:
    print "False"
