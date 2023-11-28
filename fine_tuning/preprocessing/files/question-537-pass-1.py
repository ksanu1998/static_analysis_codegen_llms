def minLength(string, l):
    return "".join(string[i] for i in range(0, len(string), l))
