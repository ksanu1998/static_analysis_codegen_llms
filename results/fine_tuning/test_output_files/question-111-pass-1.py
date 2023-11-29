def quadrant(s):
    if (s.real() > 0 and s.imag() > 0):
        print("First Quadrant")
    elif (s.real() < 0 and s.imag() > 0):
        print("Second Quadrant")
    elif (s.real() < 0 and s.imag() < 0):
        print("Third Quadrant")
    else:
        print("Fourth Quadrant")


if __name__ == "__main__":
    s = complex(1, 2)
    quadrant(s)
