n = int(input())

sieve = [True] * n

# inspect until i is equal to sqrt(n) because the greatest divider of n is less than or equal to sqrt(n)
m = int(n ** 0.5)
for i in range(2, m + 1):
   if sieve[i] == True:           # if i is a prime number,
       for j in range(i+i, n, i): # let all multiples of i to false
           sieve[j] = False

prime_number_list = [i for i in range(2, n) if sieve[i] == True]n = int(input())

sieve = [True] * n

# inspect until i is equal to sqrt(n) because the greatest divider of n is less than or equal to sqrt(n)
m = int(n ** 0.5)
for i in range(2, m + 1):
   if sieve[i] == True:           # if i is a prime number,
       for j in range(i+i, n, i): # let all multiples of i to false
           sieve[j] = False

prime_number_list = [i for i in range(2, n) if sieve[i] == True]
