def isInGivenBase(Str, base):
    if (base > 16):
        return False
    elif (base <= 10):
        for i in range(len(Str)):
            if (Str[i].isnumeric() and (ord(Str[i]) >= ord('0')
                                        and ord(Str[i]) < (ord('0') + base)) == False):
                return False

    else:
        for i in range(len(Str)):
            if (
                Str[i].isnumeric() and (
                    (ord(
                        Str[i]) >= ord('0') and ord(
                        Str[i]) < (
                    ord('0') +
                    base)) or (
                        ord(
                            Str[i]) >= ord('A') and ord(
                                Str[i]) < (
                                    ord('A') +
                                    base -
                            10))) == False):
                return False
    return True


Str = "AF87"
if (isInGivenBase(Str, 16)):
    print("Yes")
else:
    print("No")
