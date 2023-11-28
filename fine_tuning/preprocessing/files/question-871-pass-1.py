def printCubeFree(n):
    cube_free_numbers = []
    for i in range(1, n+1):
        if i**3 < n:
            cube_free_numbers.append(i)
    return cube_free_numbers
