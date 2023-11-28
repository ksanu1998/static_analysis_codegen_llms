def maxPlanes(A, B, N):
    planes = []
    for i in range(N):
        planes.append((A[i], B[i]))
    planes.sort(key=lambda x: x[0])
    count = 0
    prev_pos = planes[0][0]
    for plane in planes:
        if plane[0] - prev_pos > 1:
            count += 1
            prev_pos = plane[0]
    return count
