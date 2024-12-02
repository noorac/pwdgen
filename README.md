# Pwdgen

Pwdgen is a lightweight, customizable password generator written in Python. Designed to provide secure and flexible password generation, it supports various options for password length, character types, and special character subsets.

---

## Features

- **Customizable Password Length**: Generate passwords of any length.
- **Character Type Selection**: Choose to must include uppercase letters, lowercase letters, numbers, and special characters.
- **Special Character Subsets**: Option to use all special characters or a predefined subset for ease of typing and compatibility.
- **Secure and Practical**: Ensures strong password creation for personal or professional use.

---

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pwdgen.git
```
2. Navigate to the project directory:
```bash
cd pwdgen
```
3. Ensure Python 3.x is installed on your system.

4. Make sure the following dependencies are installed on your system:
```bash
pyperclip, xclip, wl-clipboard
```
**Note:** xclip is for X users, wl-clipboard is for wayland-users.

## Usage

Run the script with command-line arguments to specify your password preferences.
```bash
python pwdgen.py -h
```
Will produce output:
```bash
usage: pwdgen [-h] [-l int] [-s] [-c] [-u] [-n] [-p] [-a]

Generates a password of varying strength based on userinput

options:
  -h, --help  show this help message and exit
  -l int      Enter length of pwd as an integer, default 12
  -s          This flag will add all special characters to list of
              possibilities
  -c          Flag for must-have at least 1 lower case characters
  -u          Flag for must-have at least 1 upper case characters
  -n          Flag for must-have at least 1 number
  -p          Flag for must-have at least 1 special
  -a          Flag for must-have at least 1 all types
```
The following example will produce a password of length 18 characters, using all special characters, and at least one upper and one lower case character.
```bash
python pwdgen.py -l 18 -s -c -u
```
After the password is generated, it will be automatically copied to your clipboard. The script will then wait for user input to regenerate a password or to finish the script. This is so that the user can easily copy the password and test if the e.g. website will accept it or not, and a simple press of "y" will deem the password acceptable, and end the script, and any other character will regenerate a new password and copy the new password to the clipboard.

## Caution
The password is not store anywhere, and it is not possible to regenerate the same password, meaning you should probably write it down in your mind, or on a piece of paper.
