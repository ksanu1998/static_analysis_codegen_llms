def printSubsInDelimeters(string):import re

def printSubsInDelimeters(string):
    return re.findall(r"<[^>]+>", string)
