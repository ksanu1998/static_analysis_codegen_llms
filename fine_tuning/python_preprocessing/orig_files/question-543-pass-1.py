def encrypt(input_arr):
    evenPos = '@'
    oddPos = '!'
    for i in range(len(input_arr)):
        ascii = ord(input_arr[i])
        repeat = (ascii - 96)if ascii >= 97 else (ascii - 64)
        for j in range(repeat):
            if (i % 2 == 0):
                print(oddPos, end="")
            else:
                print(evenPos, end="")
        if __name__ == "__main__":
            input_arr = ['A', 'b', 'C', 'd']
            print(encrypt(input_arr))
