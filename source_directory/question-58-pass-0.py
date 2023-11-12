# Minimum LCM of all pairs in a given array. 
import sys


def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 


def lcm(a, b): 
    return (a * b) // gcd(a, b) 


def lcm_array(arr): 
    result = 1
    for x in arr: 
        result = lcm(result, x) 
    return result 


# Driver Code 
if __name__ == '__main__': 
    arr = [2, 4, 6, 8] 
    n = len(arr) 
    print("LCM of given numbers is", lcm_array(arr)) 


# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 






































































































































































































































































































