# Generate first K multiples of N using Bitwise operators. 
def Kmultiples(n, k): 
    return (n << k) - n 