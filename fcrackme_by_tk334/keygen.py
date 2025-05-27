def generate_password(username):
    length = len(username)
    if 2 <= length <= 7:
        return username + "@fsociety"
    elif length > 7:
        return "Mr." + username
    else:
        return None

def main():
    username = input("Enter your username: ")
    password = generate_password(username)
    if password:
        print(f"Generated password: {password}")
    else:
        print("Username must be at least 2 characters long.")

if __name__ == "__main__":
    main()
