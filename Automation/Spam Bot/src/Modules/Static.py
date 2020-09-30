from Modules.Spammer import *
from Modules.Colours import *
from time import sleep

def static():
    cyan("\n-----FIXED MESSAGE SPAM-----")
    print("This is the most iconic, yet basic spamming method. Spams a fixed string n times\n")
    message = input("Enter the String you want to spam \n> ")
    try:
        count = int(input("Enter the number of times you want to spam the message \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        red("ERROR : Enter Only Numbers")
        grey("Press enter to exit ")
        input()
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for i in range(count):
        spammer(message,sleep)