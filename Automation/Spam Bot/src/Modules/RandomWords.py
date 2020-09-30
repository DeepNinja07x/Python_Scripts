from Modules.Spammer import *
from Modules.Colours import *
from time import sleep
import random

def randwords(data):
    cyan("\n-----RANDOM DICTIONARY WORDS SPAM-----")
    print("This spamming method spams random dictionary words\n")
    words = data.splitlines()
    try:
        count = int(input("Enter the number of words you want to spam \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        red("ERROR : Enter Only Numbers")
        grey("Press enter to exit ")
        input()
        sys.exit(0)
    randwords = random.sample(words,count)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in randwords:
        spammer(x,sleep)