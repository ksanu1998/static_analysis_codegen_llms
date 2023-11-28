def calculate_change(length, breadth):[PYTHON]
def calculate_change(length, breadth):
    area_old = length * breadth
    area_new = length * (breadth + 10)
    change = (area_new - area_old) / area_old
    return change
