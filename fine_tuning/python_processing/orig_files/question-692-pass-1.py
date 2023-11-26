def calculate_change(length, breadth):
    change = 0
    change = length + breadth + ((length * breadth) // 100)
    return change


if __name__ == "__main__":
    cL = 20
    cB = -10
    cA = calculate_change(cL, cB)
    print(cA)
