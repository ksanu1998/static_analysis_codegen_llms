def isInGivenBase(Str, base):
    try:
        int(Str, base)
        return True
    except ValueError:
        return False
