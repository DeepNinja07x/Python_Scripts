# In try and except block, if there is an error it executes the except block.
# Else it executes the try block.
print("Example 1 : ")
try:
    age = int(input("How old are you?"))
    print("You are",age,"Years old")
    if(age<19):
        print("You are a Teenager")
except:
    print("Please enter only Numbers")      

print("\nExample 2 : ")
try:
        a = int(input("Enter the value of the numerator : "))
        b = int(input("Enter the value of the denominator : "))

        print("Result =",a/b)
except ValueError:
    print("VALUE ERROR : ENTER ONLY INTEGER NUMBERS")
except ZeroDivisionError:
    print("ZERO DIVISION ERROR : NUMBER CANNOT BE DIVIDED BY ZERO")
except : 
    print("UNKNOWN ERROR! PLEASE CHECK YOUR VALUES")

print("\nYou can also use except(error1,error2) to catch multiple exceptions in a single parameter")
input("Press any key to exit ")

