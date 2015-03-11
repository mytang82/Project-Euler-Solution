# Problem 3
# ---------
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
'''
The following solution assumes
    (LargestPrimeFactor of n) < sqrt(n)
This is not always true, for example n=6, 15, or 1194
My fixes is to continuously divide n through all prime < sqrt(n)
Then compare it with the max of all prime < sqrt(n)
'''
import math
def prime(n, primeDict = {}):
    # check whether n is a prime number, add to primeDict if it is
    if n > 2:
        if n%2 == 0:
            return False
        for i in range(3,n,2): # no need to go over even numbers
            if (n%i == 0) and (n/i != 1):
                return False
            elif n/float(i) < i:
                break
    primeDict[n] = n
    return True
    
def partFactor(n):
    # return a list of factors for n that are less than sqrt(n)
    factorL = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            factorL.append(i)
    return factorL

def LargestPrimeFactor(n):
    # return the largest prime factor of n
    factorL = partFactor(n)
    primeDict = {} # need to initialize the dictionary
    for i in factorL[1:]: # no need to check 1, the first term
        prime(i, primeDict)
    # continuously divide n through all elements in the primeDict
    count = 1
    while count > 0:
        count = 0
        for primeNum in primeDict:
            if n%primeNum == 0:
                n = n/primeNum
                count = count + 1
    # check whether m is a prime number
    prime(n, primeDict)
    return max(primeDict)

# Test cases
print prime(2)
# True
print prime(3)
# True
print prime(5)
# True
print prime(31)
# True
print prime(26)
# False
print partFactor(90)
# [1, 2, 3, 5, 6, 9]
print LargestPrimeFactor(90)
# 5
print LargestPrimeFactor(6)
# 3
print LargestPrimeFactor(15)
# 5
print LargestPrimeFactor(11940)
# 199
print LargestPrimeFactor(600851475143)
# 6857