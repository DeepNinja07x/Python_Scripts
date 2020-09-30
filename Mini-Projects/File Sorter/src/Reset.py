import pickle
import os
import time
from modules.extensions import *
from modules.colours import *

def reset():
    pickle_file = open("../assets/extensions_data.pkl", 'wb')
    pickle.dump(extensions, pickle_file)
    pickle_file.close()


if __name__ == "__main__":
    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    grey(output)
    green("\n"+"-"*20)
    version = open("../assets/version.txt" , "r").read()
    time.sleep(1)

    reset()

    green("Data Reset Successfully!")
    grey("Press any key to exit")
    input()