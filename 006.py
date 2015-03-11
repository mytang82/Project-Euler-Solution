# Problem 6
# ---------
'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''
def sumOfSquare(n):
    # sum of the squares of the first n natural numbers
    result = 0
    for i in range(1,n+1):
        result = result + (i*i)
    return result

def squareOfSum(n):
    # square of the sume of the first n natural numbers
    result = sum(range(1,n+1))**2
    return result

def sumSquareDiff(n):
    return squareOfSum(n) - sumOfSquare(n)

# Test cases
# ----------
print sumSquareDiff(10)
# 2640
print sumSquareDiff(100)
# 25164150