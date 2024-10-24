password = input("What is your password? ")

length = len(password) - 1

for char in range(length):
    if password[char] != password[length - char]:
        print("Password is not valid")
        exit(0)

print("Password " + password + " is valid")
