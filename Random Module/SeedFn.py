import random
# If you use seed function, the values generated for the same number remains same.
i = int(input("Enter a number : "))
x = random.seed(i)
y = random.random()
print(y)
input("Press any key to exit ")