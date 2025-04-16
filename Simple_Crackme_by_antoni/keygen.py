def get_password():
    enc = [0xeb, 0xc6, 0xcb, 0x8a, 0xc7, 0xcb, 0x8a, 0xc1, 0xc5, 0xde, 0xcb, 0x84]
    key = 0xaa
    password = ''.join(chr(b ^ key) for b in enc)
    return password 

if __name__ == "__main__":
    pw = get_password();
    # The password needs to be given as an argument surrounded by single quotes, otherwise the program won't read them properly
    print(pw)
