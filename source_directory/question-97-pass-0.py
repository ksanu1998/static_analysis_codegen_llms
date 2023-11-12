# Gill 's 4th Order Method to solve Differential Equations. 
from math import sqrt


def dydx(x, y): 
    return [y[1], -0.04*y[0] + 1e4*y[1]*(y[2]-y[0])]


def rk4(y, dydx, x, h): 
    k1 = h*dydx(x, y)
    k2 = h*dydx(x+0.5*h, y+0.5*k1)
    k3 = h*dydx(x+0.5*h, y+0.5*k2)
    k4 = h*dydx(x+h, y+k3)
    y = y + (k1 + 2*k2 + 2*k3 + k4)/6.0
    return y


def rk4_solve(y, dydx, x, h, n): 
    for i in range(n): 
        y = rk4(y, dydx, x, h)
        x = x + h
    return y


def main(): 
    y = [1.0, 0.0]
    x = 0.0
    h = 0.001
    n = 10000
    y = rk4_solve(y, dydx, x, h, n)
    print(y)
    print(y[0])
    print(y[1])
    print(sqrt(y[0]*y[0] + y[1]*y[1]))


if __name__ == '__main__': 
    main()


# 1.0000000000000002
# 1.0000000000000002
# 0.0
# 1.0000000000000002

# 1.0000000000000002
# 