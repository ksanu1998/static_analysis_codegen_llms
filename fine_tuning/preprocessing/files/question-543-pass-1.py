def encrypt(input_arr):
    output_arr = []
    for i in range(len(input_arr)):
        if input_arr[i] == '!':
            output_arr.append('@')
        else:
            output_arr.append('!')
    return ''.join(output_arr)
