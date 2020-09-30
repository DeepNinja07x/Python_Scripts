import os
from modules.functions import *
from modules.colours import *
import time

if __name__ == "__main__":
    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    grey(output)
    green("\n"+"-"*20)
    version = open("../assets/version.txt" , "r").read()
    cyan("File Sorter | " + version)
    time.sleep(1)
    while(True):
        print("1) Add an extension to an already existing category")
        print("2) Add an extension to a new catagory")
        print("3) Delete an extension")
        print("4) View extensions")
        print("5) Quit")
        choice = int(input("What would you like to do?\n> "))
        
        pickle_file = open("../assets/extensions_data.pkl", 'rb')
        extensions = pickle.load(pickle_file)
        pickle_file.close()

        if(choice == 1):
            add_data(extensions)
        elif(choice == 2):
            add_category(extensions)
        elif(choice == 3):
            delete_data(extensions)
        elif(choice == 4):
            view_data(extensions)
        elif(choice == 5):
            green("\n---- x Thanks for using File Sorter x ----")
            grey("Press enter to exit...")
            input()
            break
        else:
            red("\nERROR : INVALID OPTION")

        green("\n"+"-"*20)