# pwdgen:
# This program will generate passwords of varying length, and thus varying strength
# Dependency arch xclip, pyperclip


import string
import sys
import random
import pyperclip


class Pwd(object):
    """The pwd class. used to generate the password"""
    def __init__(self, length) -> None:
        self.length = length  # Num. of characters
        self.pwd_o = ""  # The output string for the password
        self.letters = list(string.ascii_letters[:26])
        self.letters_c = list(string.ascii_letters[26:])
        self.numbers = list(string.digits)
        """
        Special Characters use s_characters instead
        of s_characters_all as default. This is a subset of
        all punctuation to prevent difficult to 
        press punctuation like [ on non english keyboards.

        In the future, potentially using cmd args s_characters_all
        can be activated and used should the user want it.
        """
        self.s_characters = ["!","#","%","&","$","-",";",":","=","@"] 
        self.s_characters_all = list(string.punctuation)
        self.alternatives = self.letters + self.letters_c + self.numbers + self.s_characters
        self.pwd = []  # Each list item is a character in the password
        self.generator()  # Generate a password
        self.pwd_str()  # Turn it into a string
        return None

    def __str__(self) -> str:
        """If the object itself is called, return the pwd"""
        return self.pwd_o

    def generator (self) -> None:
        """Generate the password itself"""
        self.pwd = []  # Resets self.pwd list
        for i in range(self.length):
            self.pwd.insert(len(self.alternatives)+1,self.alternatives[random.randint(0,len(self.alternatives))-1])
        return None

    def pwd_str(self) -> None:
        """Turn the pwd_list into a str"""
        self.pwd_o = ""  # Reset output string
        for i in range(len(self.pwd)):
            self.pwd_o += str(self.pwd[i-1])
        return None


def main(argv) -> None:
    """
    Main function

    First check if a system argument was given, and try to make it an integer.
    If not an integer or no argument, set default password length to 12 chars
    """

    try:
        pwd_length = int(argv[1])
    except ValueError:
        pwd_length = 12  # Not an integer, default 12
    except IndexError:
        pwd_length = 12  # No arguments, default 12

    while True:
        new_password = Pwd(pwd_length)  # New password
        pyperclip.copy(new_password.pwd_o)  # Copy to clipboard
        print(f"New password is\n(length: {pwd_length})\n\n{new_password}\n\n(Copied to clipboard)")
        ans = input(f"Is this acceptable(anything other than 'y' will generate a new password? ")
        if ans == "y":
            break  # Pwd acceptable
        else:
            del new_password  # Pwd not acceptable, del and regen

    print("\n")
    return None


if __name__ == "__main__":
    main(sys.argv)
