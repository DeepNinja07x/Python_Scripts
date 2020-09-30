from Modules.Colours import *
from cryptography.fernet import Fernet
import sys

def password_function():

    file = open('../temp/key.temp','rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)

    try:
        with open("../temp/password.temp", 'rb') as f:
            password = f.read()
        decrypted = fernet.decrypt(password)
        decrypted = decrypted.decode()
        green("PASSWORD MANAGER")
        cyan("-" * 25)
        while(True):
            entered_password = input("Enter your password \n> ")
            if(decrypted == entered_password):
                green("Logged in successfully")
                grey("Press any key to continue...")
                input()
                break
            else:
                red("Incorrect password")
    except:
        green("PASSWORD MANAGER")
        cyan("-" * 25)
        print("Since, this is the first time you are using Password_manager, Create a password.")
        red("DO NOT FORGET THIS PASSWORD. YOU CANNOT CHANGE IT LATER.")
        
        password = input("Enter your password \n> ")
        password = password.encode()
        encrypted = fernet.encrypt(password)

        with open("../temp/password.temp", 'wb') as f:
            f.write(encrypted)

        green("Your password has been saved successfully")
        cyan("Relaunch the application to continue.")
        grey("Press enter to exit...")
        input()
        sys.exit(0)