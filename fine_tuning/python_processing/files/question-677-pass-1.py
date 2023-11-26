from math import sqrt, pow


def coneSlantHeight(cone_h, cone_r):# Calculate the slant height of the cone
    slant_height = sqrt(pow(cone_h, 2) + pow(cone_r, 2))
    return slant_height


def pyramidSlantHeight(pyramid_h, pyramid_b, pyramid_a):[/INST]
    # Calculate the slant height of the pyramid
    slant_height = sqrt(pow(pyramid_h, 2) + pow(pyramid_b, 2) + pow(pyramid_a, 2))
    return slant_height


# Test the functions with some sample values
cone_h = 5
cone_r = 3
print("Slant height of cone with height", cone_h, "and radius", cone_r, "is", coneSlantHeight(cone_h, cone_r))

pyramid_h = 10
pyramid_b = 4
pyramid_a = 3
print("Slant height of pyramid with height", pyramid_h, "base", pyramid_b, "and altitude", pyramid_a, "is", pyramidSlantHeight(pyramid_h, pyramid_b, pyramid_a))
