import re
user_string = input("Input: ")
i = 0
while i < len(user_string):
    if i+1 < len(user_string) and re.match(r'[^\w\s]', user_string[i]) and user_string[i+1].isdigit():
        char = user_string[i]*int(user_string[i+1])
        print(char, end='')
        i += 2
    elif re.match(r'[^\w\s]', user_string[i]):
        print(user_string[i], end='')
        i += 1
    else:
        i += 1
