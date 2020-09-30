import re

print("""
Modifiers or Flags : 
re.I        -> To ignore cases.
re.L        -> Interprets words according to the current locale.
re.M        -> Searches for matches from beginning or end(^ or $)
re.S        -> Does not consider a .,\\n,spaces, as string instead of special charcter.
re.U        -> Interprets characters according to the unicode characters.
re.X        -> Ignores all white spaces, except when inside a set or followed by a backslash.
""")

def check(x):
    if(x):
        print("Match Found")
    else:
        print("Match Not Found")

# re.I
pattern = "Hello"
sequence = "hello"
x = re.match(pattern,sequence,re.I) # Not Case Sensitive Anymore
check(x)

# re.M
pattern = "Hello \n World"
sequence = "Hello \n World"
x = re.match(pattern,sequence,re.M) # Considers even if the line ends.
check(x)

input("Press any key to exit ")
