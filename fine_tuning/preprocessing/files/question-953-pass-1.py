def minToggle(arr, n):
    # Initialize variables
    toggle_count = 0
    first_zero_index = -1
    last_one_index = n

    # Iterate through the array
    for i in range(n):
        # If the current element is 0 and it is not the first 0, then toggle
        if arr[i] == 0 and i!= first_zero_index:
            toggle_count += 1
        # If the current element is 1 and it is not the last 1, then toggle
        elif arr[i] == 1 and i!= last_one_index:
            toggle_count += 1
        # If the current element is 0 and it is the first 0, then update the first_zero_index
        if arr[i] == 0 and first_zero_index == -1:
            first_zero_index = i
        # If the current element is 1 and it is the last 1, then update the last_one_index
        if arr[i] == 1 and i == n - 1:
            last_one_index = i

    return toggle_count
