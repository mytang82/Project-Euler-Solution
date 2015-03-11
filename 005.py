# Problem 5
# ---------
'''
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.  What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
'''
primeL = [2,3,5,7,11,13,17,19] # list of prime numbers < 20

def primeFactor(n, factorDict={}):
    # return a list of prime factors for n
    for i in primeL:
        if n%i == 0:
            if i not in factorDict:
                factorDict[i] = 1
            else:
                factorDict[i] = factorDict[i]+1
            if (n/i in primeL) and (n/i not in factorDict):
                factorDict[n/i] = 1
            elif (n/i in primeL) and (n/i in factorDict):
                factorDict[n/i] = factorDict[n/i] + 1
            else:
                factorDict = primeFactor(n/i, factorDict)
            break
    return factorDict

def smallestMultiple(n):
    '''
    return the smallest positive number that is evenly divisible by all of the
    numbers from 1 to n
    '''
    factorDict = {}
    for i in range(1,n+1):
        tempDict = primeFactor(i, {})
        for primeNum in tempDict.keys():
            if factorDict.get(primeNum) == None: # primeNum not in factorDict
                factorDict[primeNum] = tempDict[primeNum]
            else:
                factorDict[primeNum] = max(factorDict[primeNum],tempDict[primeNum])
    result = 1
    for j in factorDict.keys():
        result = result * (j**factorDict[j])
    return result

# Test cases
# ----------
for i in range(1,11):
    print 'i =', i, primeFactor(i, {})
'''
i = 1 {}
i = 2 {2: 1}
i = 3 {3: 1}
i = 4 {2: 2}
i = 5 {5: 1}
i = 6 {2: 1, 3: 1}
i = 7 {7: 1}
i = 8 {2: 3}
i = 9 {3: 2}
i = 10 {2: 1, 5: 1}
'''
print smallestMultiple(10)
# 2520
print smallestMultiple(20)
# 232792560
