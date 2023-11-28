import numpy as np
import sys
RODS = 3
N = 3
dp = np .zeros((N + 1, RODS + 1, RODS + 1))


def initialize():
    global dp
    dp = np.zeros((N + 1, RODS + 1, RODS + 1))
