import string

def generate_password(username):
    return str(sum(ord(c) for c in username))

if __name__ == "__main__":
    username = input("Enter username: ")
    password = generate_password(username)
    print(f"Password: {password}")
