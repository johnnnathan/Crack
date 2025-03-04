
def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)


text = input("Enter the string: ")
key = int(input("Enter the key (0-255): "))  
result = xor_encrypt_decrypt(text, key)

print("XOR result:", result)
