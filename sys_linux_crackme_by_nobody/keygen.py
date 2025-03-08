def reverse_serial():
    target = 0x70707
    for password in range(0, 0x1000000):
        local_20 = (password & 0xff) | 0x37
        uVar2 = ((password & 0xff0000) - 0x610000) ^ 0x150000
        uVar1 = (local_20 // 0x11) + ((password & 0x1f00) ^ 0x1e00)
        if (uVar2^ uVar1) == target:
            print (f"Found password: {password: #010x}") 
            return password
    print("No matching password found.")
    return None
# Run the reverse process
reverse_serial()
