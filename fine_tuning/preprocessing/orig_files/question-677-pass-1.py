from math import sqrt, pow


def coneSlantHeight(cone_h, cone_r):
    slant_height_cone = sqrt(pow(cone_h, 2) + pow(cone_r, 2))
    print("Slant height of cone is:", slant_height_cone)


def pyramidSlantHeight(pyramid_h, pyramid_s):
    slant_height_pyramid = sqrt(pow(pyramid_s / 2, 2) + pow(pyramid_h, 2))
    print("Slant height of pyramid is:", "{:.5f}".format(slant_height_pyramid))


if __name__ == '__main__':
    H1 = 4.5
    R = 6
    coneSlantHeight(H1, R)
    H2 = 4
    S = 4.8
    pyramidSlantHeight(H2, S)
