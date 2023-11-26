def isReducible(Str):
    while "10" in Str:
        Str = Str.replace("10", "")
    return Str == ""
