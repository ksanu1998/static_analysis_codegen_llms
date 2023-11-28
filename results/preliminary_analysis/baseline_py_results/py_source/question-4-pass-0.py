# Check if an integer is rotation of another given integer. 
import math


def check(A, B): 
	
	if A == B: 
		return True
	
	if A == 0 or B == 0: 
		return False
	
	if A < 0 or B < 0: 
		return False
	
	if A == 1 or B == 1: 
		return True
	
	if A < B: 
		return check(A, B % A) 
	else: 
		return check(B, A % B) 


# Driver Code 
A = 10
B = 20
print(check(A, B)) 