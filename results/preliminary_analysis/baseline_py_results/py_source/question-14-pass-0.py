# Construct longest possible sequence of unique elements with given LCM. 
from math import sqrt, ceil, floor


def constructArrayWithGivenLCM(N): 
    # Find LCM of 1 to N 
    lcm = 1
    for i in range(1, N + 1): 
        lcm = (lcm * i) // gcd(lcm, i) 
  
    # Construct array 
    arr = [] 
    for i in range(1, N + 1): 
        arr.append(i) 
  
    # Repeat elements of array to get LCM 
    for i in range(N, lcm): 
        arr.append(arr[i % N]) 
  
    return arr 


def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 


# Driver code 
N = 10
print("LCM of 1 to", N, "is", constructArrayWithGivenLCM(N)[-1]) 


# Output:
# LCM of 1 to 10 is 360