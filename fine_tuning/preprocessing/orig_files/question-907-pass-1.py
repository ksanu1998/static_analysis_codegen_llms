def kmphTOmph(kmph):
    mph = 0.6214 * kmph
    return mph


def mphTOkmph(mph):
    kmph = (float)(mph * 1.60934)
    return kmph


/*Driver code to check the above function * /
kmph = 150
mph = 100
print "speed in miles / hr is ", kmphTOmph(kmph)
print "speed in km / hr is ", mphTOkmph(mph)
