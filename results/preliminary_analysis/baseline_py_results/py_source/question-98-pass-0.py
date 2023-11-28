# Program to print numbers from N to 1 in reverse order. 
def PrintReverseOrder(N): 
    if N > 0: 
        PrintReverseOrder(N-1) 
        print(N) 

# Driver Code 
N = 5
PrintReverseOrder(N) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
