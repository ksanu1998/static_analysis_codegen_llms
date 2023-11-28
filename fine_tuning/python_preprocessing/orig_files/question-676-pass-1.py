def lengthOfLatusRectum(A, B):
    major = 2.0 * A
    minor = 2.0 * B
    latus_rectum = (minor * minor) / major
    return latus_rectum


if __name__ == "__main__":
    A = 3.0
    B = 2.0
    print('%.5f' % lengthOfLatusRectum(A, B))
