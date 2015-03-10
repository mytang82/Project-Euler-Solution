# Problem 3
# ---------
import math
def prime(n, primeDict = {}):
    # check whether n is a prime number, add to primeDict if it is
    for i in range(2,n):
        if n%i == 0:
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
    primeDict = {} # need to initialize an empty dictionary
    for i in factorL[1:]: # no need to check 1, the first term
        prime(i, primeDict)
    return max(primeDict)

print prime(31)
# True
print prime(26)
# False
print partFactor(90)
# [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90]
print LargestPrimeFactor(90)
# 5
print LargestPrimeFactor(600851475143)
# 6857

