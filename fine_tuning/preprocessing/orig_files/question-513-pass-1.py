import re


def RemoveHTMLTags(strr):
    print(re .compile(r '<[^>]+>').sub('', strr))


if __name__ == '__main__':
    strr = "<div><b>Geeks for Geeks</b></div>"
    RemoveHTMLTags(strr)
