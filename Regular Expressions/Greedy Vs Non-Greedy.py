import re

print("""Greedy Finds all the matches and prints them all,
In non greedy function, moment one function is encountered, it returns.""")

pattern = "Hello"
sequence = "Hello world"
sequence1 = r'<h1>Title<\h1>'
print("Greedy. Matches the entire text between the first and last : ")
x = re.match(r'<.*>',sequence1).group()             # Greedy
print(x)
print("Non Greedy. Matches the first and next and then prints it : ")
x = re.match(r'<.*?>',sequence1).group()            # Non-Greedy
print(x)

input("Press any key to exit ")