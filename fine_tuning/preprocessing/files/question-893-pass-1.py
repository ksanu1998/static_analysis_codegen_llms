def maxArea(A):
    max_area = 0
    left = 0
    right = len(A) - 1
    while left < right:
        width = right - left
        height = min(A[left], A[right])
        area = width * height
        if area > max_area:
            max_area = area
        if A[left] < A[right]:
            left += 1
        else:
            right -= 1
    return max_area
