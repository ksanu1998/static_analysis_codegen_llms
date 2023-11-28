# Product of N terms of a given Geometric series. 
def productOfGP(a, r, n): 
    p = 1
    for i in range(n): 
        p = p * (a / (1 - r)) 
    return p 
  
# Driver Code 
a = 2
r = 0.5
n = 5
print("Product of GP is", productOfGP(a, r, n)) 

# Output:
# Product of GP is 1.6000000000000002