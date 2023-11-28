import sys
import math


def maxLength(s, n):
    right = 0
    left = 0
    coun = 0
    max_length = -(sys .maxsize - 1)
    s = s + '1'
    for i in range(0, n + 1):
        if s[i] == 'o':
            coun += 1
        else:
            if coun > max_length:
                right = 0
                left = 0
                if s[i] == 'x':
                    right = 1
                if i - coun > 0 and s[i - coun - 1] == 'x':
                    left = 1
                coun = math .ceil(float(coun / (right + left)))
                max_length = max(max_length, coun)
            coun = 0
    return max_length


if __name__ == '__main__':
    s = "oooxoooooooooxooo"
    n = len(s)
    print(maxLength(s, n))
