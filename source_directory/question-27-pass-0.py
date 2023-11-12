# Find the value of P and modular inverse of Q modulo 998244353. 
def calculate(p, q): 
    # Calculate the value of P and Q 
    P = p 
    Q = q 
    # Calculate the value of phi(P) 
    phi = (P - 1) * (Q - 1) 
    # Calculate the value of e 
    e = 7 
    # Calculate the value of d 
    d = modinv(e, phi) 
    return (P, Q, e, d) 
  
# Driver Code 
if __name__ == '__main__': 
    # Call the function to calculate the value of P, Q, e and d 
    (P, Q, e, d) = calculate(1000000007, 1000000009) 
    print("P = ", P) 
    print("Q = ", Q) 
    print("e = ", e) 
    print("d = ", d) 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat