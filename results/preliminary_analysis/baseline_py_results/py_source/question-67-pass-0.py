# Find the sum of the first N Centered heptagonal number. 
def center_heptagonal_num(n): 
    return (n * (3 * n - 1)) / 2 
  
# Driver Code 
n = 10
print("Sum of the first", n, "Centered Heptagonal Number is", 
      center_heptagonal_num(n)) 
