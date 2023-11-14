import math



def check(A, B):
    if A == B:
        return True
    if A < B:
        return False
    if math.floor(math.log10(A)) + 1!= len(str(A)):
        return False
    return str(A) in str(B)
