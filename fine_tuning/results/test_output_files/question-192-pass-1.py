def decideWinner(a, n):
    if (n == 1):
        return 1
    if (n == 2):
        if (a[0] > a[1]):
            return 1
        else:
            return 2
    if (n == 3):
        if (a[0] > a[1]):
            if (a[0] > a[2]):
                return 1
            else:
                return 2
        else:
            if (a[1] > a[2]):
                return 2
            else:
                return 3
    if (n == 4):
        if (a[0] > a[1]):
            if (a[0] > a[2]):
                if (a[0] > a[3]):
                    return 1
                else:
                    return 3
            else:
                if (a[1] > a[3]):
                    return 2
                else:
                    return 4
        else:
            if (a[1] > a[2]):
                if (a[1] > a[3]):
                    return 2
                else:
                    return 4
            else:
                if (a[2] > a[3]):
                    return 3
                else:
                    return 4
    if (n == 5):
        if (a[0] > a[1]):
            if (a[0] > a[2]):
                if (a[0] > a[3]):
                    if (a[0] > a[4]):
                        return 1
                    else:
                        return 4
                else:
                    if (a[1] > a[4]):
                        return 2
