def overflow(H, r, h, N, R):
    # Calculate the volume of the water tank
    V = H * R

    # Calculate the volume of each solid ball
    V_ball = (4.0 / 3.0) * 3.14 * (r ** 3)

    # Calculate the total volume of the solid balls
    V_balls = V_ball * N

    # Check if the total volume of the solid balls is greater than the volume of the water tank
    if V_balls > V:
        return True
    else:
        return False
