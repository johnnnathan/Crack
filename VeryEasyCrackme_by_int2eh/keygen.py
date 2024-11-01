# This script is useless, don't use it outside of wanting to see how the un-used transformation happens 
#
# Have a great day :)
# By github.com/johnnnathan 

un_used_password = ""
string = "YourPass"
key = 10

for char in string:
    character = ord(char)
    character ^= key 
    password = un_used_password+ chr(character)

print(un_used_password)
