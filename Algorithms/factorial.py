def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

number = int(input("Enter value of n: "))
print(f"Factorial of {number} is {factorial(number)}")