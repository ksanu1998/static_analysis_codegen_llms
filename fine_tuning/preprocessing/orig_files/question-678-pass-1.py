from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def lengthOfLatusRectum(a, b, c):
    vertex = [(-b / (2 * a)), (((4 * a * c) - (b * b)) / (4 * a))]
    focus = [(-b / (2 * a)), (((4 * a * c) - (b * b) + 1) / (4 * a))]
    print(
        "{:.6f}".format(
            4 *
            distance(
                focus[0],
                focus[1],
                vertex[0],
                vertex[1])))


if __name__ == "__main__":
    a = 3
    b = 5
    c = 1
    lengthOfLatusRectum(a, b, c)
