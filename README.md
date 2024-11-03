
# Pwgen

Pwdgen is a simple python script that will generate a string of varying length consisting of random letters, digits and special characters using several sets of alternatives.

## Installation

Download and use as a script for now

## Usage

python3 pwdgen.py [-h] [-l int] [-s] 

Generates a password of varying strength based on userinput

options:
  -h, --help  show this help message and exit
  -l int      Enter length of pwd as an integer, default 12
  -s          This flag will add all special characters to list of possibilities


After a pwd has been generated, it is copied to the clipboard. Should the password be acceptable, press 'y'. Pressing any other key will regenerate the password. The reason for this is to quickly paste and see if the e.g. website accepts the password, or if any of the special characters are deemed unusable, or if it requires capital letters, numbers etc. For the time being there are no checks that the passwords generated contain at least one character from each set. 

After the program exits, the password is not stored in any way, and cannot be recovered. Keep this in mind, and consider writing the password down, for example in your mind or in the physical space.


## License

GNU General Public License v3.0
