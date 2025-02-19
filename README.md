# ZIP File Brute Force Cracker

## Overview
This script attempts to crack password-protected ZIP files using a brute-force approach. It generates combinations of characters and tests them as passwords until the correct one is found.

## Features
- Supports both digits (0-9) and letters (a-z, A-Z) for password combinations.
- Saves previously guessed passwords to a wordlist file (`wordlist.txt`) to avoid re-trying the same passwords.
- Allows the user to specify the maximum password length.
- Checks saved passwords first before starting the brute-force attack.

## Prerequisites
Ensure you have Python installed (version 3.6 or newer).

## Usage
1. Clone or download the repository.
2. Navigate to the script's directory.
3. Run the following command:

```bash
python brute_force_zip.py
```

4. Enter the required information when prompted:
   - **ZIP file path:** Provide the path to the password-protected ZIP file.
   - **Maximum password length:** Specify the longest password length you want to test.

## Code Explanation

### Key Functions

- **save_password(password):** Appends guessed passwords to `wordlist.txt`.
- **load_saved_passwords():** Reads previously guessed passwords from `wordlist.txt`.
- **try_password(zip_file, password):** Attempts to extract the ZIP file using a given password.
- **brute_force_zip(zip_path, max_length):** Iterates through all possible combinations of characters up to `max_length` and tries them as passwords.
- **main():** Handles user input and kicks off the brute-force attack.

### Character Set
The script uses the following characters for password generation:

```python
chars = string.digits + string.ascii_letters  # 0-9, a-z, A-Z
```

## Disclaimer
This script is for educational purposes only. Do not use it for any illegal activities. Cracking passwords without permission is unethical and, in most cases, illegal.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to open an issue or reach out.

