import math



def isConcentrichexagonal(N):
    # Check if N is a perfect square
    if math.sqrt(N) % 1 == 0:
        # Get the square root of N
        square_root = int(math.sqrt(N))
        # Check if the number of edges in the hexagon is equal to the number of edges in the regular hexagon with the same side length
        if len(hexagon_edges(square_root)) == len(hexagon_edges(N)):
            return True
    return False

def hexagon_edges(N):
    # Return a list of the edges of the hexagon with the given side length
    return [N * math.cos(math.radians(60)) + N * math.cos(math.radians(120)), N * math.cos(math.radians(60)) - N * math.cos(math.radians(120)), -N * math.cos(math.radians(60)) + N * math.cos(math.radians(120)), -N * math.cos(math.radians(60)) - N * math.cos(math.radians(120))]
