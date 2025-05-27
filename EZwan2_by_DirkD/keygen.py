def get_password():
  message = "Congratulations you did it!"
  enc_string = 0x32b6e514
  password = ""

  for _ in range(8):
    index = enc_string & 0xf
    password += message[index]
    enc_string >>= 4

  return password 

print("Password is: ", get_password())
