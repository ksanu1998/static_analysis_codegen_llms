def toList(string):
    l = []
    for x in string:
        l .append(x)
    return l


def toString(l):
    return ''.join(l)


def stringFilter(string):
    n = len(string)
    i = -1
    j = 0
    while j < n:
        if j < n - 1 and string[j] == 'a' and string[j + 1] == 'c':
            j += 2
        elif string[j] == 'b':
            j += 1
        elif i >= 0 and string[j] == 'c' and string[i] == 'a':
            i -= 1
            j += 1
        else:
            i += 1
            string[i] = string[j]
            j += 1
    i += 1
    return toString(string[:i])


string1 = "ad"
print "Input => " + string1 + "NEW_LINEOutput=>",
print stringFilter(toList(string1)) + "NEW_LINE"
string2 = "acbac"
print "Input => " + string2 + "NEW_LINEOutput=>",
print stringFilter(toList(string2)) + "NEW_LINE"
string3 = "aaac"
print "Input => " + string3 + "NEW_LINEOutput=>",
print stringFilter(toList(string3)) + "NEW_LINE"
string4 = "react"
print "Input => " + string4 + "NEW_LINEOutput=>",
print stringFilter(toList(string4)) + "NEW_LINE"
string5 = "aa"
print "Input => " + string5 + "NEW_LINEOutput=>",
print stringFilter(toList(string5)) + "NEW_LINE"
string6 = "ababaac"
print "Input => " + string6 + "NEW_LINEOutput=>",
print stringFilter(toList(string6)) + "NEW_LINE"
string7 = "abc"
print "Input => " + string7 + "NEW_LINEOutput=>",
print stringFilter(toList(string7)) + "NEW_LINE"
