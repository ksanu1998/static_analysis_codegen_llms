def findNthRoot(x, n):
    x = float(x)
    n = int(n)
    if (x >= 0 and x <= 1):
        low = x
        high = 1
    else:
        low = 1
        high = x
    epsilon = 0.00000001
    guess = (low + high) / 2
    while abs(guess ** n - x) >= epsilon:
        if guess ** n > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    print(guess)


x = 5
n = 2
findNthRoot(x, n)
