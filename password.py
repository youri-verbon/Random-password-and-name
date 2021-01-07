import random
import pyperclip
import pylint
import names


def main():
    menu()

def menu():

    choice = input("A: Password generator \nB: Name generator \n\nPlease enter your choice: ")

    if choice == "A" or choice =="a":
        password()
    elif choice =="B" or choice =="b":
        name()
    else:
        print("\nError, this is not a valid entry.\nPlease try again.\n") + main()

def password():
    chars = "ABCDEFGIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz1234567890!@#$%*"
    count = input("\nHow many characters long?:\n\n")
    count = int(count)

    x = 0
    result = [""]
    while x < count:
        password = random.choice(chars)
        x += 1
        print(password, end = "")
        result.append(password)


    result = ''.join(str(e) for e in result)
    pyperclip.copy(result)
    what = input("\n\nFor what is the password?: ")
    my_file = open("passwords.txt","a+")
    my_file.write("\n" + what + "\n" + result + "\n")

def name():
    nametype = input("\nA: Full name \nB: First name \nC: Last name\n\n")
    
    if nametype == "A" or nametype =="a":
        fullname = ("\n" + names.get_full_name())
        print(fullname)
        pyperclip.copy(fullname)
        input("\nPress ENTER to exit")
    elif nametype == "B" or nametype == "b":
        firstname = ("\n" + names.get_first_name())
        print(firstname)
        pyperclip.copy(firstname)
        input("\nPress ENTER to exit")
    elif nametype == "C" or nametype == "c":
        lastname = ("\n" + names.get_last_name())
        print(lastname)
        pyperclip.copy(lastname)
        input("\nPress ENTER to exit")
    else:
        print("Error, this is not a valid entry.\nPlease try again.\n") + main()

main()





