import sys


def myAtoi(str):
    if not str:
        return 0
    str = str.strip()
    if not str.isdigit() and str[0] not in ["-", "+"]:
        return 0
    if str[0] == "-":
        sign = -1
        str = str[1:]
    else:
        sign = 1
    if not str.isdigit():
        return 0
    result = 0
    for c in str:
        result = result * 10 + int(c)
        if result * sign < -2147483648 or result * sign > 2147483647:
            return 2147483647
    return result * sign
