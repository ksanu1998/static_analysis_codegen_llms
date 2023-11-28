from math import sqrt


def checkPolygonWithMidpoints(arr, N, midpoints):
    # Calculate the distance between each midpoint and the center of the circle
    distances = [sqrt((midpoints[i][0] - arr[N // 2][0]) ** 2 + (midpoints[i][1] - arr[N // 2][1]) ** 2) for i in range(N)]

    # Check if the distances between the midpoints and the center of the circle are all equal
    return all(distance == distances[0] for distance in distances)
