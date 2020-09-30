from Modules.Spammer import *
from Modules.Colours import *
from time import sleep

def numbers():
    cyan("\n-----SEQUENTIAL NUMBERS SPAM-----")
    print("This is a spam method that sends numbers from 1 to n as seperate messages\n")
    try:
        count = int(input("Enter the number until which you want to spam \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        red("ERROR : Enter Only Numbers")
        grey("Press enter to exit ")
        input()
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(1,count+1):
        x = str(x)
        spammer(x,sleep)