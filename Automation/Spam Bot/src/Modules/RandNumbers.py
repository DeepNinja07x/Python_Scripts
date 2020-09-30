from Modules.Spammer import *
from Modules.Colours import *
from time import sleep
import random
import sys

def randomnum():
    cyan("\n-----LARGE NUMBERS SPAM-----")
    print("This spamming method spams random numbers from 1 - 999999999 each as a seperate message\n")
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
        num = random.randint(1,999999999)
        term = str(num)
        spammer(term,sleep)