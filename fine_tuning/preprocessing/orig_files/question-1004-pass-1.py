def getMinSteps(K):
    return bin(K).count("1")


n = 343
print(getMinSteps(n))
