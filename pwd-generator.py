# This program will generate passwords of varying length, and thus varying strength
# Dependency arch xclip, pyperclip

# Better cmd args, main triggers function to import pwds if exists, load list into object file

import sys
import random
import pyperclip

###Functions###

def new_pwd(pwd_length):
    """ This function runs a continous loop of generating objects of the 
    pwd-class. If the password generated is not acceptable, it will be 
    deleted, and a new one made until one is accetable"""
    cont = True
    while cont:
        new_password = pwd(pwd_length)
        pyperclip.copy(new_password.pwd_o)
        print(f"New password(length: {pwd_length}) is\n\n{new_password}\n\n(Copied to clipboard)")
        ans = input(f"Is this acceptable(anything other than 'y' will generate a new password? ")
        if ans=="y":
            cont = False
            return new_password
        else:
            del new_password

###Classes###

class pwd:
    """The pwd class. used to generate the password"""
    def __init__(self, length) -> None:
        self.length = length
        self.pwd_o = ""
        self.alternatives = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9,"!","#","%","&","$","-",";",":","=","@"]
        self.pwd = []
        self.generator()
        self.pwd_str()
        return None

    def __str__(self):
        """If the object itself is called, return the pwd"""
        return self.pwd_o

    def generator (self):
        """Generate the password itself"""
        #Reset self.pwd
        self.pwd = []
        i = 1
        for i in range(self.length):
            self.pwd.insert(len(self.alternatives)+1,self.alternatives[random.randint(0,len(self.alternatives))-1])
            i += 1
        return 0

    def pwd_str(self):
        """Turn the pwd_list into a str"""
        #Reset self.pwd_o(output)
        self.pwd_o = ""
        i = 1
        for i in range(len(self.pwd)):
            self.pwd_o += str(self.pwd[i-1])
            i += 1
        return 0






###Main###

def main(argv):
    """Main function

    First check if a system argument was given, and try to make it an integer.
    If not an integer or no argument, set default password length to 12 chars"""
    try:
        pwd_length = int(argv[1])
    except ValueError:
        pwd_length = 12  # Not an integer, default 12
    except IndexError:
        pwd_length = 12  # No arguments, default 12

    pwd_obj_list = []
    pwd_obj_list.append(new_pwd(pwd_length))

    #Exit
    print("\n")
    return 0

if __name__ == "__main__":
    main(sys.argv)
