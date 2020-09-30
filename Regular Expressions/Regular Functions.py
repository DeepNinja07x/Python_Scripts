import re
import string
print("""
Different Regular Functions are : 
re.compile(pattern, flags)           -> Compiles the pattern to be matched
re.search(pattern, string, flags)    -> Searches through the string for exact match
re.match(pattern, string, flags)     -> Checks if there is a match between pattern and string
re.split(pattern, string, max, flag) -> Splits the string based on the pattern provided
re.findall(pattern, string, flag)    -> Prints all the matches found using the pattern
re.finditer(pattern, string, flags)  -> Returns the string as an iterable object
re.sub(pattern, repl, string, count) -> Replaces the string with the pattern
re.subn(pattern, repl, string, count)-> Does the same thing as re.sub but returns it in a tuple(string and count)
re.escape(pattern)                   -> Escapes all characters other than ascii characters
""")

print("Using the re.compile function")
pattern = "Hello world"
x = re.compile(pattern)
y = x.match("Hello world")
if (y):
    print("Strings match")
else:
    print("Strings do not match")

print("\nMatching without using the compile function : ")
pattern = "Hello world"
x = re.match(pattern,"Hello World")
if (y):
    print("Strings match")
else:
    print("Strings do not match")

print("\nUsing the Split Function : ")
x = re.split("\W+","Hello,World")   # W to start from the left and + to keep moving forward.
print(x)
x = re.split("(\W+)","Hello,World")   # W to start from the left and + to keep moving forward, braces will print ,
print(x)

print("\nUsing the findall function")
x = re.findall(r"Hello","Hello World")  # Checks and prints matches.
print(x)

print("\nUsing the sub function")
x = re.sub(r"there","World","Hello there. Python is fun.")  # Checks if there is present and then replaces it with world.
print(x)

print("\nUsing the subn function")
x = re.subn(r"there","World","Hello there. Python is fun. Hello there")
print(x)

print("\nUsing the escape function")
pattern = string.ascii_lowercase
x = re.escape(pattern)
print(x)
pattern = string.digits
x = re.escape(pattern)
print(x)
pattern = "+-*$^&#"
x = re.escape(pattern)
print(x)

input("Press any key to exit ") 