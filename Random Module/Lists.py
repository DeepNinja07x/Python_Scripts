import random
# Picking an element from a list randomly
x = ["Blue","Green","Red","Yellow","Black","White"]

y = random.sample(x,3)        # Picks 3 Samples from the given list(x).
print(y)

y = random.choices(x)         # Picks a Single value from the given list(x).
print(y)
input("Press any key to exit ")