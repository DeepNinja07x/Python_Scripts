# In finally clause, is the final message printed to the user even if you got an exception.
# Note : Be it you got an error or not, Finally clause would still show message to user.

try:
    a = int(input("Hey! How old are you?"))
    b = int(input("How long have you been coding? "))
except:
    print("ERROR : PLEASE ENTER THE CORRECT VALUES")
else:
    if(a<15 and b>=1):
        print("Hey! You are only",a,"years old and you already have coding experiance of",b,"years!")
    else:
        print("Hey! You are",a,"years old with a coding experiance of",b,"years!")
finally:
    print("PROGRAM TERMINATED")                 # Irrespective of conditions, this statement is always run.
input("Press any key to exit ")