def findSum(str1):import re

def findSum(str1):
    numbers = re.findall(r'\d+', str1)
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum
