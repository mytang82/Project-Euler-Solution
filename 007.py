# Problem 7
# ---------
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10,001st prime number?
'''

def prime(n):
    primeList = [2,3,5,7,11,13] # first 6 prime numbers
    if n <= len(primeList):
        return primeList[n-1]
    largest = primeList[len(primeList)-1] + 2 # start with the next uneven number
    primeInd = 0 # 0 ==> prime number, >0 ==> not prime number
    while len(primeList) < n:
        for prime in primeList:
            if (largest % prime) == 0: # largest is not a prime number
                largest = largest + 2 # no need to check even numbers
                primeInd = primeInd + 1
                break
        # all prime numbers in primeList have been checked
        if primeInd == 0: # a prime number
            primeList.append(largest)
            largest = largest + 2 # no need to check even numbers
        else:
            primeInd = 0 # not a prime number, need to reset my indicator
    return primeList[n-1]

# Test cases
# ----------
print prime(6)
# 13
print prime(10001)
# 104743