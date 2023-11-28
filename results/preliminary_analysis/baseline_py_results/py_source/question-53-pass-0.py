# Check if A can be converted to B by reducing with a Prime number. 
def isPossible(A, B): 
    if A == B: 
        return True
    if A < B: 
        return False
    while A > B: 
        if A % 2 == 0: 
            A = A // 2
        elif A % 3 == 0: 
            A = A // 3
        else: 
            return False
    return True

# Driver Code 
A = 12
B = 15
print(isPossible(A, B)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)