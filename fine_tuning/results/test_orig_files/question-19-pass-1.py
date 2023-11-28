def findMode(a, n):

def findMode(a, n):
    # Initialize variables to keep track of mode and count
    current_mode = a[0]
    current_count = 1
    max_count = 1
    for i in range(1, n):
        if a[i] == current_mode:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_mode = a[i]
            current_count = 1
    return current_mode
