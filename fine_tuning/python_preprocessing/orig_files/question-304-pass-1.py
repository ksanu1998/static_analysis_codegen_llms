def Bits(kilobytes):
    Bits = kilobytes * 8192
    return Bits


def Bytes(kilobytes):
    Bytes = kilobytes * 1024
    return Bytes


if __name__ == "__main__":
    kilobytes = 1
    print(
        kilobytes,
        "Kilobytes =",
        Bytes(kilobytes),
        "Bytes and",
        Bits(kilobytes),
        "Bits")
