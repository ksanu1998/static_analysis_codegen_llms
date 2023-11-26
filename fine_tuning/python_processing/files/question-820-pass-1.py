def decode(s):
    if not s:
        return ''
    count = int(s[0])
    substring = s[1:1+count]
    return substring + decode(s[1+count:])
