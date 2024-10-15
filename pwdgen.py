# pwdgen:
# This program will generate passwords of varying length, and thus varying strength
# Dependency arch xclip, pyperclip


import string
import sys
import random
import pyperclip
import argparse


def toggle_flags(arg) -> bool:
    if arg:
        arg = True
    elif not arg:
        arg = False
    return arg


class Pwd(object):
    """The pwd class. used to generate and store the password"""

    def __init__(self, length, use_all_special) -> None:
        self.length = length  # Num. of characters
        self.use_all_special = use_all_special  # Use all special characters
        self.pwd_o = ""  # The output string for the password
        self.letters = list(string.ascii_letters[:26])
        self.letters_c = list(string.ascii_letters[26:])
        self.numbers = list(string.digits)
        # Decide to use all special characters or not
        if self.use_all_special is True:
            self.s_characters = list(string.punctuation)
        elif self.use_all_special is False:
            self.s_characters = ["!", "#", "%", "&", "$", "-", ";", ":", "=", "@"]
        # Put all  options into one big bowl
        self.alternatives = self.letters + self.letters_c + self.numbers + self.s_characters
        self.pwd = []  # Each list item is a character in the password
        self.generator()  # Generate a password
        self.pwd_str()  # Turn it into a string
        return None

    def __str__(self) -> str:
        """If the object itself is called, return the pwd"""
        return self.pwd_o

    def generator(self) -> None:
        """Generate the password itself"""
        self.pwd = []  # Resets self.pwd list
        for i in range(self.length):
            self.pwd.insert(len(self.alternatives)+1, self.alternatives[random.randint(0, len(self.alternatives))-1])
        return None

    def pwd_str(self) -> None:
        """Turn the pwd_list into a str"""
        self.pwd_o = ""  # Reset output string
        for i in range(len(self.pwd)):
            self.pwd_o += str(self.pwd[i-1])
        return None


def main(argv) -> None:
    """
    Main function::
    First check if a system argument was given, and try to make it an integer.
    If not an integer or no argument, set default password length to 12 chars
    """
    # Create parser object
    parser = argparse.ArgumentParser(
        prog="pwdgen",
        description="Generates a password of varying strength based on userinput",
        epilog="Try again")
    parser.add_argument("-l", metavar="int", type=str, help="Enter length of pwd as an integer, default 12")
    parser.add_argument("-s", help="This flag will add all special characters to list of possibilities",
                        action="store_const", const=True)
    parser.add_argument("-c", help="Flag for must-have at least 1 lower case characters", action="store_const", const=False)
    parser.add_argument("-u", help="Flag for must-have at least 1 upper case characters", action="store_const", const=False)
    parser.add_argument("-n", help="Flag for must-have at least 1 number", action="store_const", const=False)
    parser.add_argument("-p", help="Flag for must-have at least 1 special", action="store_const", const=False)
    parser.add_argument("-a", help="Flag for must-have at least 1 all types", action="store_const", const=False)
    args = parser.parse_args()

    # Check for length argument
    if args.l is None:
        pwd_length = 12
    else:
        try:
            pwd_length = int(args.l)
        except ValueError:
            print("ValueError: invalid argument for -l. Expected <type> int")
            print(parser.print_help())
            exit()

    # Check for all special characters argument
    use_all_special = toggle_flags(args.s)
    # Check for min requirements, store requirements in a list
    # Contents are: lower, upper, number, special
    min_requirements = []
    min_requirements.append(toggle_flags(args.c))
    min_requirements.append(toggle_flags(args.u))
    min_requirements.append(toggle_flags(args.n))
    min_requirements.append(toggle_flags(args.p))

    # Check if the all flag was used, and set all in min_requirements to True if all flag was used
    min_one_each = toggle_flags(args.a)
    if min_one_each:
        for i in range(len(min_requirements)):
            min_requirements[i] = True
    elif not min_one_each:
        pass

    while True:
        new_password = Pwd(pwd_length, use_all_special)  # New password
        pyperclip.copy(new_password.pwd_o)  # Copy to clipboard
        print(f"New password(length: {new_password.length}, all_special: {new_password.use_all_special})\n\n{new_password}\n")
        ans = input(f"(Copied to clipboard, y to exit, any to regenerate)")
        if ans == "y":
            break  # Pwd acceptable
        else:
            del new_password  # Pwd not acceptable, del and regen

    print("\n")
    return None


if __name__ == "__main__":
    main(sys.argv)
