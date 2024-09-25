# Keygen to Licence Keygen By 999
# 
# Another .NET program. We will use dotPeek just as we did for "dotqw's first crackme". 
# I put the application in the program and started searching for objects that I could use to find the password.
# This crackme uses a gui which makes it easier to detect value handling. I found a method by the name of "GenerateSerialKey" and knew
# I was close. I looked at the contents of the method and it divided the key into three segments. The first segment 
# was the basic username, the second the username with "salt1" appended to it and the third one the username with "salt2" appended to it.
# GenerateSegment was the function that handled all the logic behind the key generation. Since we do not have to deal with assembly, or 
# pseudocode we can easily transform the .NET code into usable python code.
#
# It computes the sha256 hash of the individual segment and then iterates over the first two indexes of the hash while doing some 
# calculations. It mods the value of the character on the current intex and the one at an offset of 2, using the value 36.
# Then it takes the ASCII code and through a simple if statement, calculates the values that the segment's key should consist of.
# 
# Example:
#   Username: abcd
#   Key     : S2W3-I0WI-D9LM
# 
#
# Have a great day :)
# github.com/johnnnathan

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


