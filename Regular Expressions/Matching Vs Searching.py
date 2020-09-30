import re

print("Example 1 : ")
pattern = 'd'
sequence = 'abcdef'

x = re.match(pattern,sequence)
y = re.search(pattern,sequence)

print(y.group())
try:
    print(x.group())
except:
    print("Using the match function will now return any value. "+ 
    "This is because it seaches from first, and if it is false prints false")

print("Example 2 : ")
pattern = 'a'
pattern1 = 'd'
sequence = 'abcdef'

x = re.match(pattern,sequence)
y = re.search(pattern1,sequence)

if x:
    print("Match Found")
else:
    print("Match not found")

if y:
    print("Match Found")
else:
    print("Match not found")

input("Press any key to exit ")