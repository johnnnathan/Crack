string = "+!,*`.|{/)x/.`+,}z`y|t,`/(u}`}ty{y,|.}(tz"

key = 77
final_string = ""


for char in string:
    ascii_value = ord(char)
    xored_value = ascii_value ^ key
    final_string += chr(xored_value)


# I know that for some reason the 2 turns into a c, I do not know why that happens to it only. Performing the operation manually 
# using the values inside the cpu registers gives the proper output.
print("Key : " + str(key))
print("Pass value: " + final_string)
print("Should be : flag-216bd5bc-fa07-419a-be80-09464a1c0e97")
