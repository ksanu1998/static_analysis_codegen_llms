import sys


def myAtoi(Str):
    sign, base, i = 1, 0, 0
    while (Str[i] == ' '):
        i += 1
    if (Str[i] == '-' or Str[i] == '+'):
        sign = 1 - 2 * (Str[i] == '-')
        i += 1
    while (i < len(Str) and Str[i] >= '0' and Str[i] <= '9'):
        if (base > (sys .maxsize // 10) or (base ==
                                            (sys .maxsize // 10) and (Str[i] - '0') > 7)):
            if (sign == 1):
                return sys .maxsize
            else:
                return -(sys .maxsize)
        base = 10 * base + (ord(Str[i]) - ord('0'))
        i += 1
    return base * sign


Str = list(" -123")
val = myAtoi(Str)
print(val)
