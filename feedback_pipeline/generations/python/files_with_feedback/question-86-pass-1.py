def isAutoBiographyNum(number):
    root = math.sqrt(number)
    if root == int(root):
        # Check if the number is a Autobiographical Number
        if number % (root + 1) == 0:
            return True
    return False
