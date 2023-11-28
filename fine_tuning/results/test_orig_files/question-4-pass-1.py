import math



def check(A, B):
    if A == B:
        return True
    if A < B:
        B = B * 10
        while B!= A:
            B = B // 10
            B = B * 10 + A % 10
            A = A // 10
    else:
        A = A * 10
        while A!= B:
            A = A // 10
            A = A * 10 + B % 10
            B = B // 10
    return A == B
