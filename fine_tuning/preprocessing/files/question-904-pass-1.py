def nthSHN(n, dp):import math

def nthSHN(n, dp):
    if n == 1:
        return 1
    else:
        return round(math.sqrt(2) * nthSHN(n-1, dp) / math.sqrt(n+1), dp)
