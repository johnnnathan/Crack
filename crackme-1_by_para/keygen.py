from itertools import product
import string

def operate_upon(key):
    length = 0
    result = 0

    while key[length] != '\0':
        length += 1

    length_2 = length  

    i = 0

    while i <= length_2 - 1:
        result = (ord(key[i]) + (result << 6)) % 0x989680
        i += 1


    return result



def find_input_for_result(target_result, max_length=5):

    possible_chars = string.ascii_letters + string.digits + string.punctuation + ' '

    for length in range(1, max_length + 1):
        for combination in product(possible_chars, repeat=length):
            key = ''.join(combination) + '\0'  
            result = operate_upon(key)
            if result == target_result:
                return ''.join(combination)

    return None

target_result = 0x54a337

found_input = find_input_for_result(target_result, max_length=5)

if found_input:
    print(f"Found input: {found_input}")
else:
    print("No matching input found within the given length range.")
