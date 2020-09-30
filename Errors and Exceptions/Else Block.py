# else block runs if exception block does not run!
try:
    age = int(input("Enter your age : "))
except ValueError:
    print("VALUE ERROR: ENTER ONLY INTEGER NUMBERS")
else:
    print("You are",age,"Years old")
    try:
        exp = int(input("How many years have you been coding? "))
    except:
        print("VALUE ERROR: ENTER YEARS IN NUMBERS ONLY")
    else:
        if(age<15 and exp>=1):
            print("Awesome! You are only",age,"and you've already coded for",exp,"years long!")
        else:
            print("You have a coding experiance of",exp,"years")
input("Press any key to exit ")