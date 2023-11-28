# Form the Cubic equation from the given roots. 
def findEquation(a, b, c): 
    # Find the coefficients of the equation. 
    # The coefficients are the roots of the equation. 
    # The coefficients are in the form of a^3 + b*a^2 + c*a + d = 0 
    d = -a 
    a = b 
    b = c 
    c = d 
  
    # The equation is now formed. 
    # The equation is in the form of ax^3 + bx^2 + cx + d = 0 
    return a, b, c, d 
  
# Driver code 
if __name__ == "__main__": 
    # The coefficients of the equation. 
    a = 1
    b = 2
    c = 3
  
    # The roots of the equation. 
    x1 = 0
    x2 = 0
    x3 = 0
  
    # The equation is in the form of ax^3 + bx^2 + cx + d = 0 
    a, b, c, d = findEquation(a, b, c) 
  
    # The roots of the equation are found using the Cardano's method. 
    x1, x2, x3 = cardano(a, b, c, d) 
  
    # The roots are printed. 
    print("The roots of the equation are: ", end = "") 
    print(x1, x2, x3) 
  
    # The equation is printed. 
    print("The equation is: ", end = "") 
    print(a, "x^3 + ", b, "x^2 + ", c, "x + ", d, " = 0") 
  
    # The discriminant of the equation is printed. 
    print("The discriminant of the equation is: ", end = "") 
    print(discriminant(a, b, c, d)) 
  
    # The value of the equation at x = 1 is printed. 
    print("The value of the equation at x = 1 is: ",