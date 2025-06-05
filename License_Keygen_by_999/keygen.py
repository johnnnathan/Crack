
from hashlib import sha256

username = input("What is your username?\n")

def get_segment(input):
    hash__ = sha256(input.encode())
    hash = hash__.digest()
    segment_key = ""
    for i in range(2):
        num1 = hash[i] % 36
        num2 = hash[i + 2] % 36
        ch1 = chr(48 + num1) if num1 < 10 else chr(65 + (num1 - 10))
        ch2 = chr(48 + num2) if num2 < 10 else chr(65 + (num2 - 10))
        segment_key = segment_key + ch1 + ch2

    print(segment_key)
    return(segment_key)

segment2_input = username + "salt1"
segment3_input = username + "salt2"

key = get_segment(username) + "-" + get_segment(segment2_input) + "-" +  get_segment(segment3_input)
print("License key is :" + key)


