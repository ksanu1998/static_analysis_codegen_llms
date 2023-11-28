from math import sqrt


def distance(x1, y1, x2, y2):# Calculate the distance between two points
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_latus_rectum(a, b, c):[/INST]
    # Find the length of the latus rectum of a parabola
    return abs(2 * a)


def main():[/INST]
    # Test the find_latus_rectum function
    print(find_latus_rectum(1, 2, 3))


if __name__ == "__main__":
    main()
