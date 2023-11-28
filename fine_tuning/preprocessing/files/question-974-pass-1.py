one = [
    "",
    "one ",
    "two ",
    "three ",
    "four ",
    "five ",
    "six ",
    "seven ",
    "eight ",
    "nine ",
    "ten ",
    "eleven ",
    "twelve ",
    "thirteen ",
    "fourteen ",
    "fifteen ",
    "sixteen ",
    "seventeen ",
    "eighteen ",
    "nineteen "]
ten = [
    "",
    "",
    "twenty ",
    "thirty ",
    "forty ",
    "fifty ",
    "sixty ",
    "seventy ",
    "eighty ",
    "ninety "]


def numToWords(n, s):
    if n == 0:
        return ""
    if n < 20:
        return one[n] + s
    if n < 100:
        return ten[n // 10] + numToWords(n % 10, " ")
    if n < 1000:
        return numToWords(n // 100, "hundred ") + numToWords(n % 100, "")
    if n < 1000000:
        return numToWords(n // 1000, "thousand ") + numToWords(n % 1000, "")
    if n < 1000000000:
        return numToWords(n // 1000000, "million ") + numToWords(n % 1000000, "")
    if n < 100000000000
