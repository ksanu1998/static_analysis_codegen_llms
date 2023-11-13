# Evaluate the expression ( N1 * ( N. 
mod = 1000000007


def ValOfTheExpression(n): 
    # Base Case 
    if n == 0: 
        return 0
    # If n is odd, multiply n with result of 
    # (n-1) 
    if n % 2!= 0: 
        return (n * ValOfTheExpression(n - 1)) % mod 
    # If n is even, multiply n with result of 
    # (n/2) 
    else: 
        return (ValOfTheExpression(n / 2) * 
                ValOfTheExpression(n / 2)) % mod 


# Driver Code 
n = 1000000007
print(ValOfTheExpression(n)) 