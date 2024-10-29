string = "+!,*`.|{/)x/.`+,}z`y|t,`/(u}`}ty{y,|.}(tz"

key = 77
final_string = ""


for char in string:
    ascii_value = ord(char)
    xored_value = ascii_value ^ key
    final_string += chr(xored_value)


print("Key : " + str(key))
print("Pass value: " + final_string)
print("Should be : flag-216bd5bc-fa07-419a-be80-09464a1c0e97")
