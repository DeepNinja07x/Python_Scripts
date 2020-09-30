import re

matching_sequence = r"[0-9]"

while(True):
    x = input("Enter your password : ")
    r = re.search(matching_sequence,x)
    if (r and len(x)>6):
        print(x + " is a valid password")
    else:
        print(x + " is not a valid password. Password MUST be atleast 7 characters with atleast 1 number")

input("Press any key to exit ")