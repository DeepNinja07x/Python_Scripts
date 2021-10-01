#!/usr/bin/python3

def problem(n):
    print(n, "   ")
    if( n==1 ):
        return 0
    elif( n%2==0 ):
        n = int(n/2)
    else:
        n = 3*n+1
    problem(n)


n = int(input("Enter any number : "))
problem(n)
