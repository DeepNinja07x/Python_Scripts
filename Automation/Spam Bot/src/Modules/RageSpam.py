from Modules.Colours import *
from Modules.Spammer import *
from time import sleep
import random
import string

def message():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    num = random.randint(5,10)
    spam = ""
    for x in range(num):
        spam = spam + "".join(random.choice(chars))
    return(spam)

def rage():
    cyan("\n-----RAGE SPAM-----")
    print("Rage spam is just a combination of random letters and numbers that make no sense.",
    "\nUsed primarily only for the purpose of absolute spam.\n")
    try:
        count = int(input("Enter the number of spam messages you want to send \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        red("ERROR : Enter Only Numbers")
        grey("Press enter to exit ")
        input()
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(count):
        msg = message()
        spammer(msg,sleep)