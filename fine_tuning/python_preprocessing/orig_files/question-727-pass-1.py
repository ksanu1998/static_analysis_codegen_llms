def overflow(H, r, h, N, R):
    tank_cap = 3.14 * r * r * H
    water_vol = 3.14 * r * r * h
    balls_vol = N * (4 / 3) * 3.14 * R * R * R
    vol = water_vol + balls_vol
    if vol > tank_cap:
        print("Overflow")
    else:
        print("Not in overflow state")


H = 10
r = 5
h = 5
N = 2
R = 2
overflow(H, r, h, N, R)
