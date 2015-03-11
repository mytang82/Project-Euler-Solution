# Problem 9
# ---------
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Facts we know:
    1) a+b+c = n
    2) a^2 + b^2 = c^2
    Therefore ==> a,b,c at most ~n/2
'''
import math

def perfectSquare(n):
    # generate a dict of squares up to n^2
    squareDict = {}
    for i in range(1, n+1):
        squareDict[i*i] = True
    return squareDict

def pythagoreanTripletSum(n):
    '''
    Find the pythagorean triplet that sums to n
    Since a+b+c = n AND a^2 + b^2 = c^2, a,b,c at most n/2
    '''
    squareDict = perfectSquare(n/2)
    squareList = squareDict.keys()
    result = []
    for i in range(len(squareList)-1):
        for j in range(i+1,len(squareList)):
            a2 = squareList[i]
            b2 = squareList[j]
            c2 = a2 + b2
            if (c2 in squareList) and \
              (math.sqrt(a2)+math.sqrt(b2)+math.sqrt(c2) == n):
                result.append([math.sqrt(a2),
                                math.sqrt(b2),
                                math.sqrt(c2),
                                math.sqrt(a2)+math.sqrt(b2)+math.sqrt(c2),
                                math.sqrt(a2*b2*c2)])
    return result

# Test cases
# ----------
# 1)  3,4,5 ==> n=3+4+5=12
print pythagoreanTripletSum(12)
# [[3.0, 4.0, 5.0, 12.0, 60.0]]
print pythagoreanTripletSum(1000)
# 2)  a,b,c ==> n=a+b+c=1000
# [[200.0, 375.0, 425.0, 1000.0, 31875000.0]]

  