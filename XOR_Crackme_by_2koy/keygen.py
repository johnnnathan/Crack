string = "2f39243c38382a1b393e04" 
key = 75

final_password = ""


for ASCII in range(0, len(string), 2):
    # Get the two hex values that form an ASCII symbol
    hex_pair = string[ASCII : ASCII + 2]

    # Translate the hex value to decimal notation
    decimal_value = int(hex_pair, 16)

    # Perform the XOR operation using the key (0x4b or 0d75)
    result = decimal_value ^ key

    # Turn the ASCII code into the ASCII symbol
    character = chr(result)

    # Append the resulting ASCII symbol to the start of the string to reverse its little-Endianness
    final_password = character + final_password

# print the Resulting, and stored, password. Should be "OurPassword"
print(final_password)
