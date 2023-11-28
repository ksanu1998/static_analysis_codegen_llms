# Program to check if N is a Octagonal Number. 
from math import sqrt


def isoctagonal(N): 
    x = int(sqrt(N)) 
    return (x * (x + 1) == 2 * N) 


def main(): 
    N = int(input("Enter a number: ")) 
    if isoctagonal(N): 
        print("Yes") 
    else: 
        print("No") 


#