
# pwgen

pwdgen is a simple python script that will generate a string of varying length consisting of random letters, digits and special characters using a set of alternatives.

## Installation

Download and use as a script for now

## Usage

'''bash
python3 pwdgen.py x
'''

Where x represents the number of characters desired for the length of the password. If no value is given, it defaults to 12 characters

After a pwd has been generated, it is copied to the clipboard. Should the password be acceptable, press 'y'. Pressing any other key will regenerate the password. The reason for this is to quickly paste and see if the e.g. website accepts the types of characters etc. 

After the program exits, the password is not stored in any way, and cannot be recovered. Keep this in mind, and consider writing the password down, for example in your mind or in the physical space.

## License

GNU General Public License v3.0
