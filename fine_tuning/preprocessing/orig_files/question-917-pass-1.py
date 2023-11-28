def recDigSum(n):
    if n == 0:
        return 0
    else:
        if n % 9 == 0:
            return 9
        else:
            return n % 9


def check(n):
    n = recDigSum(n)
    if n == 2 or n == 3 or n == 5 or n == 7:
        print "Yes"
    else:
        print "No"


n = 5602
check(n)
