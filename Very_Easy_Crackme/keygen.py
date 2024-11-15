# Solution to "Very Easy Crackme" by vasa
#
#
# This is not an orthodox keygen, instead of creating the Password dynamically the password is always the product of a simple rule
# Vasa uses puts(), scanf, and most importantly strcat. This concatenates one string with another.
# strcat uses the local_78 and local_10 variables. local_78 in this case, for me, is the username and local_10 a value that 
# is stored in hex. If we turn the hex into a string we will get the value of "0xjfkD2". This means that each password will be just 
# the string with that value added to it at the end. Quite simple. 
#
# Have a great day :)
# 
# By github.com/johnnnathan 


username = input("What is your username?\n")
username += "0xjfkD2"
print("Password : " + username)
