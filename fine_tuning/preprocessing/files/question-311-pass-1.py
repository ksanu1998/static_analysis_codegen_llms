digits = []
vis = [False for i in range(170)]
dp = [[[[0 for l in range(170)]for k in range(2)]
       for j in range(19)]for i in range(19)]


def convert_into_digit(n):
    return int(str(n)[:-1])
