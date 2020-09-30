import random

# We use randint function to generate numbers between a fixed range with both the extremes being inclusive
x = random.randint(0,10)        # [0,10]
print(x)

x = random.randint(-20,-10)     # Negative numbers
print(x)

x = random.randrange(0,10)      # [0,10) -> 10 is not included in the range
print(x)

# We can also print float values.
x = random.uniform(0,10.0)      # Prints Floating point values
print(x)
input("Press any key to exit ")