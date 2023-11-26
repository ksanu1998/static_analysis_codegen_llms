def finalPosition(move):
    x = 0
    y = 0
    for m in move:
        if m == "U":
            y += 1
        elif m == "D":
            y -= 1
        elif m == "L":
            x -= 1
        elif m == "R":
            x += 1
    return (x, y)
