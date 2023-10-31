# Minimum steps to convert X to Y by repeated division and multiplication. 
def solve(X, Y): 
    if X == Y: 
        return 0
    if X < Y: 
        return -1
    count = 0
    while (X!= Y): 
        if (X % 2 == 0 and Y % 2 == 0): 
            X = X / 2
            Y = Y / 2
            count += 1
        elif (X % 2!= 0 and Y % 2!= 0): 
            X = 3 * X + 1
            Y = 3 * Y + 1
            count += 1
        elif (X % 2 == 0): 
            X = X / 2
            count += 1
        else: 
            X = 3 * X + 1
            count += 1
    return count 
  
# Driver Code 
X = 100
Y = 10
print("Minimum steps to convert X to Y is", solve(X, Y)) 
  
# This code is contributed by Rajat Mishra 




















































































































































































































































