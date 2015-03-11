# Problem 10
# ----------
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
# ideas come from Problem 7
import math
import time

def prime(n):
    # return list of prime numbers less than n
    startTime = time.time() # use to time my program
    if n <= 2:
        return []
    elif n == 3:
        return [2]
    # followings are for n >= 4
    primeList = [2] # first prime number
    largest = 3 # start with the next uneven number
    primeInd = 0 # 0 ==> prime number, >0 ==> not prime number
    while largest < n:
        for prime in primeList[1:]: # do not need the 2
            if prime > math.sqrt(largest): # only need to check up to sqrt(largest)
                break
            elif (largest % prime) == 0: # largest is not a prime number
                primeInd = primeInd + 1
                break
        # all needed prime numbers in primeList have been checked
        if primeInd == 0: # a prime number
            primeList.append(largest)
        else:
            primeInd = 0 # not a prime number, need to reset my indicator       
        largest = largest + 2 # no need to check even numbers
    print time.time() - startTime # use it to time my program
    return primeList

def sumPrime(n):
    # sum of all the primes below n
    return sum(prime(n))

# Test cases
# ----------
print sumPrime(10)
# time = 0.0
# 17
print sumPrime(10000)
# time = 0.0199999809265
# 5736396
print sumPrime(100000)
# time = 1.05400013924
# 454396537
print sumPrime(2000000)
# time = 372.830999851
# 142913828922
