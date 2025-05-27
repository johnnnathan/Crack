def modify(input_string):
    modified_string = ""
    l = len(input_string)
    
    for char in input_string:
        mod_char = chr((ord(char) ^ 4 ) + l)
        modified_string += mod_char
    return modified_string
    
input_string = input("Enter string: ")
result = modify(input_string)
print("Password: ", result)
