## Keygen for "Interesting Crackme" by BananaGrease
## 
## Have a great day :)
## github.com/johnnnathan

name = list(input("Give the username: "))


for i in range(13):
    name += " "


for char in range(len(name)):
    name[char] = chr(char + ord(name[char]))

print(name)
