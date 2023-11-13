# Program to check if N is a Concentric Hexagonal Number. 
import math


def isConcentrichexagonal(N): 
    # Check if N is a perfect square 
    if (math.sqrt(N) % 1 == 0): 
        return False

    # Check if N is a perfect cube 
    if (math.pow(N, 1.0/3) % 1 == 0): 
        return False

    # Check if N is a perfect 5th root 
    if (math.pow(N, 1.0/5) % 1 == 0): 
        return False

    # Check if N is a perfect 6th root 
    if (math.pow(N, 1.0/6) % 1 == 0): 
        return False

    # Check if N is a perfect 7th root 
    if (math.pow(N, 1.0/7) % 1 == 0): 
        return False

    # Check if N is a perfect 8th root 
    if (math.pow(N, 1.0/8) % 1 == 0): 
        return False

    # Check if N is a perfect 9th root 
    if (math.pow(N, 1.0/9) % 1 == 0): 
        return False

    # Check if N is a perfect 10th root 
    if (math.pow(N, 1.0/10) % 1 == 0): 
        return False

    # Check if N is a perfect 11th root 
    if (math.pow(N, 1.0/11) % 1 == 0): 
        return False

    # Check if N is a perfect 12th root 
    if (math.pow(N, 1.0/12) % 1 == 0): 
        return False

    # Check if N is a perfect 13th root 
    if (math.pow(N, 1.0/13) % 1 == 0): 
       