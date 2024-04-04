import hashlib

# Dictionary to store user credentials
users = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add user to dictionary
    users[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if user exists
    if username in users:
        # Hash the input password for comparison
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

        # Compare hashed passwords
        if hashed_input_password == users[username]:
            print("Login successful!")
            return True
        else:
            print("Invalid password!")
    else:
        print("User not found!")

    return False

def secured_page():
    print("Welcome to the secured page!")

# Simulating a secured page
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secured_page()
                break
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
