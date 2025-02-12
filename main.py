import zipfile
from itertools import product
import string

GUESSED_PASSWORDS_FILE = "guessed_passwords.txt"

def save_password(password):
    """Save the guessed password to a file."""
    with open(GUESSED_PASSWORDS_FILE, "a") as f:
        f.write(password + "\n")

def load_saved_passwords():
    """Load already guessed passwords from the file."""
    try:
        with open(GUESSED_PASSWORDS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def try_password(zip_file, password):
    """Try extracting the ZIP file with the given password."""
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f"[SUCCESS] Password found: {password}")
        return True
    except (RuntimeError, zipfile.BadZipFile):
        return False

def brute_force_zip(zip_path, max_length):
    """Try all combinations of passwords up to max_length."""
    chars = string.digits + string.ascii_letters  # 0-9, a-z, A-Z
    saved_passwords = load_saved_passwords()

    with zipfile.ZipFile(zip_path, 'r') as zf:
        # Check saved passwords first
        print("[INFO] Checking saved passwords...")
        for password in saved_passwords:
            if try_password(zf, password):
                return password

        print("[INFO] Starting brute force...")
        for length in range(1, max_length + 1):
            for pwd_tuple in product(chars, repeat=length):
                password = ''.join(pwd_tuple)
                if try_password(zf, password):
                    save_password(password)
                    return password
                save_password(password)  # Save the guessed password even if incorrect

    print("[FAILED] No password found with brute force.")
    return None

def main():
    print("404 Pass Not Found")
    zip_path = input("Enter the path to the ZIP file: ")
    max_length = int(input("Enter the maximum password length to try: "))

    brute_force_zip(zip_path, max_length)

if __name__ == "__main__":
    main()
import zipfile
from itertools import product
import string

GUESSED_PASSWORDS_FILE = "wordlist.txt"

def save_password(password):
    """Save the guessed password to a file."""
    with open(GUESSED_PASSWORDS_FILE, "a") as f:
        f.write(password + "\n")

def load_saved_passwords():
    """Load already guessed passwords from the file."""
    try:
        with open(GUESSED_PASSWORDS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def try_password(zip_file, password):
    """Try extracting the ZIP file with the given password."""
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f"[SUCCESS] Password found: {password}")
        return True
    except (RuntimeError, zipfile.BadZipFile):
        return False

def brute_force_zip(zip_path, max_length):
    """Try all combinations of passwords up to max_length."""
    chars = string.digits + string.ascii_letters  # 0-9, a-z, A-Z
    saved_passwords = load_saved_passwords()

    with zipfile.ZipFile(zip_path, 'r') as zf:
        # Check saved passwords first
        print("[INFO] Checking saved passwords...")
        for password in saved_passwords:
            if try_password(zf, password):
                return password

        print("[INFO] Starting brute force...")
        for length in range(1, max_length + 1):
            for pwd_tuple in product(chars, repeat=length):
                password = ''.join(pwd_tuple)
                if try_password(zf, password):
                    save_password(password)
                    return password
                save_password(password)  # Save the guessed password even if incorrect

    print("[FAILED] No password found with brute force.")
    return None

def main():
    print("404 Pass Not Found")
    zip_path = input("Enter the path to the ZIP file: ")
    max_length = int(input("Enter the maximum password length to try: "))

    brute_force_zip(zip_path, max_length)

if __name__ == "__main__":
    main()
