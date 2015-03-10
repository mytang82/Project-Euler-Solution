# Problem 1
# ---------
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sum3or5(n):
    numList = []
    for num in range(n):
        if (num%3)==0 or (num%5)==0:
            numList.append(num)
    return sum(numList)

print sum3or5(10)
# 23
print sum3or5(1000)
# 233168