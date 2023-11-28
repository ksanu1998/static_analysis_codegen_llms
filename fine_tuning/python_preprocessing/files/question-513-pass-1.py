import re


def RemoveHTMLTags(strr):import re

def RemoveHTMLTags(strr):
    return re.sub(r'<.*?>', '', strr)
