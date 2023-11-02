import getpass
import base64
import json

# Function to store the username and encrypted password in a local storage file
def store_user_credentials(username, password, storage_file):
    # Encrypt the password (You should use a secure encryption method)
    encrypted_password = base64.b64encode(password.encode()).decode()

    # Load existing data or initialize an empty dictionary
    try:
        with open(storage_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Store the username and encrypted password in the dictionary
    data[username] = encrypted_password

    # Save the updated data to the local storage file
    with open(storage_file, 'w') as file:
        json.dump(data, file)

# Function to check if the entered password is correct
def is_password_correct(username, entered_password, storage_file):
    try:
        # Load stored data from the local storage file
        with open(storage_file, 'r') as file:
            data = json.load(file)

            if username in data:
                # Retrieve the stored encrypted password
                stored_password = data[username]

                # Decrypt the stored password (You should use the corresponding decryption method)
                decrypted_password = base64.b64decode(stored_password).decode()

                # Compare the entered password with the stored password
                return entered_password == decrypted_password
    except FileNotFoundError:
        pass

    # Return False if the username is not found in the file or file doesn't exist
    return False

# Main menu
def main_menu():
    while True:
        print("Choose an option:")
        print("1. Store user credentials")
        print("2. Check if a credential is correct")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            store_user_credentials(username, password, storage_file)
            print("Credentials stored in local storage.")
        elif choice == "2":
            username = input("Enter the username to check: ")
            entered_password = getpass.getpass("Enter the password to verify: ")
            if is_password_correct(username, entered_password, storage_file):
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    storage_file = "local_storage.json"  # Local storage file
    main_menu()
