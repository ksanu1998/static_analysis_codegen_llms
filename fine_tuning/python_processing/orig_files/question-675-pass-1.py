from math import sqrt, floor


def finalPosition(a, b, M):
    n = 0
    s = 0
    e = 0
    w = 0
    p = 'N'
    for i in range(M):
        if (p == 'N'):
            if (a[i] == 'U'):
                p = 'N'
                n = n + b[i]
            elif (a[i] == 'D'):
                p = 'S'
                s = s + b[i]
            elif (a[i] == 'R'):
                p = 'E'
                e = e + b[i]
            elif (a[i] == 'L'):
                p = 'W'
                w = w + b[i]
        elif (p == 'S'):
            if (a[i] == 'U'):
                p = 'S'
                s = s + b[i]
            elif (a[i] == 'D'):
                p = 'N'
                n = n + b[i]
            elif (a[i] == 'R'):
                p = 'W'
                w = w + b[i]
            elif (a[i] == 'L'):
                p = 'E'
                e = e + b[i]
        elif (p == 'E'):
            if (a[i] == 'U'):
                p = 'E'
                e = e + b[i]
            elif (a[i] == 'D'):
                p = 'W'
                w = w + b[i]
            elif (a[i] == 'R'):
                p = 'S'
                s = s + b[i]
            elif (a[i] == 'L'):
                p = 'N'
                n = n + b[i]
        elif (p == 'W'):
            if (a[i] == 'U'):
                p = 'W'
                w = w + b[i]
            elif (a[i] == 'D'):
                p = 'E'
                e = e + b[i]
            elif (a[i] == 'R'):
                p = 'N'
                n = n + b[i]
            elif (a[i] == 'L'):
                p = 'S'
                s = s + b[i]
    ver_disp = n - s
    hor_disp = e - w
    displacement = floor(
        sqrt((ver_disp * ver_disp) + (hor_disp * hor_disp)) + 1)
    print(displacement, p)


if __name__ == '__main__':
    A = ['U', 'R', 'R', 'R', 'R']
    B = [1, 1, 1, 1, 0]
    N = len(A)
    finalPosition(A, B, N)
