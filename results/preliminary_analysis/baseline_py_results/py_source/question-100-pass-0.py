# Program to find if two numbers and their AM and HM are present in an array using STL. 
from math import sqrt


def ArithmeticMean(A, B): 
    return (A + B) / 2


def HarmonicMean(A, B): 
    return 2 / (1 / A + 1 / B)


def check(A, B, C, D): 
    if (A == C and B == D): 
        return True
    if (A == D and B == C): 
        return True
    return False


def main(): 
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n): 
        arr.append(int(input()))
    arr.sort()
    for i in range(n - 1): 
        for j in range(i + 1, n): 
            if (check(arr[i], arr[j], ArithmeticMean(arr[i], arr[j]), HarmonicMean(arr[i], arr[j]))): 
                print("Yes")
                return
    print("No")


# Using the special variable
# __name__
if __name__ == "__main__": 
    main()

#