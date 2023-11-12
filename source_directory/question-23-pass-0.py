# Least Square Regression Line. 
def calculateB(x, y, n): 
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_xx = 0
    for i in range(n): 
        sum_x += x[i] 
        sum_y += y[i] 
        sum_xy += x[i]*y[i] 
        sum_xx += x[i]*x[i] 
    b = (n*sum_xy - sum_x*sum_y)/(n*sum_xx - sum_x*sum_x) 
    return b 
  
# Driver Code 
if __name__ == '__main__': 
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    n = len(x) 
    b = calculateB(x, y, n) 
    print("Slope =", b) 
    print("Intercept =", calculateA(b, x, y, n)) 
    print("y =", calculateA(b, x, y, n), "x +", b) 
    print("y =", calculateA(b, x, y, n), "x +", b, "=", calculateA(b, x, y, n) + b*x[0]) 
    print("y =", calculateA(b, x, y, n), "x +", b, "=", calculateA(b, x, y, n) + b*x[1]) 
    print("y =", calculateA(b, x, y, n), "x +", b, "=", calculateA(b, x, y, n) + b*x[2]) 
    print("y =", calculateA(b, x, y, n), "x +", b, "=", calculateA(b, x, y, n) + b*x[3]) 
   