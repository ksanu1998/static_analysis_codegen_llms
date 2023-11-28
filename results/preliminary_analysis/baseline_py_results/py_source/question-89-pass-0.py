# Determine whether the given integer N is a Peculiar Number or not. 
def sumDig(n): 
    sum = 0
    while(n>0): 
        sum += n%10
        n //= 10
    return sum 
  
# Driver Code 
n = 123456789
if(sumDig(n) == n): 
    print("Yes")
else: 
    print("No") 

# Output:
# Yes

# Time Complexity: O(logN)
# Space Complexity: O(1)
