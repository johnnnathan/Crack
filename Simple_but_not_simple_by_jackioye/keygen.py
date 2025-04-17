input_string = "v`fw`qUdvvrjwa476"
xor_key = 5

xor_result = ''.join(chr(ord(char) ^ xor_key) for char in input_string)

print("Decrypted String: ", xor_result)
