import numpy as np


def MaximumMarks(marksarr, timearr, h, n, p):
    # Sort the marks array in descending order
    marksarr.sort(reverse=True)

    # Initialize variables to store the maximum marks and the corresponding time
    max_marks = 0
    max_time = 0

    # Iterate through the marks array
    for i in range(len(marksarr)):
        # Calculate the time required to study the current topic
        time_required = int(marksarr[i] / p)

        # Check if the current topic can be studied within the given time
        if time_required <= timearr[i]:
            # Update the maximum marks and time if the current topic is better than the previous one
            if marksarr[i] > max_marks:
                max_marks = marksarr[i]
                max_time = time_required

    # Return the maximum marks and time
    return max_marks, max_time
