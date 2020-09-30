print("\nExample 1 : ")
rate = int(input("On a scale of 1-10 how much would you rate Python : "))
if(rate<1 or rate>10):
    raise Exception("ERROR : ONLY VALUE BETWEEN 1-10 IS ACCEPTED")
else:
    print("You have rated Python for",rate)

print("\nExample 2 : ")
try:
    rate = int(input("On a scale of 1-10 how much would you rate Python : "))
    if(rate<1 or rate>10):
        raise ValueError
except ValueError:
    print("ERROR : ONLY VALUE BETWEEN 1-10 IS ACCEPTED")
else:
    print("You have rated Python for",rate)
input("Press any key to exit ")