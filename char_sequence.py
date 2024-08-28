# character sequence
str_val = input('Enter the input: ')


def get_sequence(str_input):
    final_str = ''
    char_print = ''
    for i in range(len(str_input)):
        char = str_input[i]
        if char.isdigit():
            final_str += char_print * int(char)
        else:
            char_print = char
            if i+1 < len(str_input) and not str_input[i+1].isdigit():
                final_str += char_print
    return final_str


print(f'Output sequence is: ', get_sequence(str_val))
