# Solution to "Hyperion" by Chriswerwerwer
#
# The program takes in a username. Then it iterates over all of the characters inside the username and sums up the ASCII values.
# Then the sum is mod-ed by 10 and the resulting value needs to be both the length of the password, and also the final character of it.
# The other characters in the password are unimportant and can be whaveter you please. I used "0" for simplicity.
# Have a great day :)
#
# github.com/johnnnathan


username = input("What is your username?\n")
sum = 0

for char in username:
    sum += ord(char)

sum %= 10
for x in range(sum - 1):
    password += "0"
password += str(sum)
print(password)
