import math



def smallestNumber(N):
    if N == 1:
        return 1
    else:
        return N * math.ceil(N / 10 ** (len(str(N)) - 1))
