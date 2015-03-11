# -*- coding: utf-8 -*-
# Problem 4
# ---------
'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def prodTwo(n):
    # generate a number list made from the product of two numbers from 1 to n
    result = []
    for i in range(1,n+1):
        for j in range(i,n+1):
            result.append(i*j)
    return result

def palindrome(n):
    # test whether n is a palindrome -- read the same both way
    nstr = str(n)
    # i=index starts from 0
    # j=index starts from len(nstr)-1
    j = len(nstr)-1
    for i in range(len(nstr)/2):
        if i == j: # len is 1 OR middle index of odd len
            break
        elif i+1 == j: # len is even
            if nstr[i] != nstr[j]:
                return False
        else:
            if nstr[i] != nstr[j]:
                return False
            else:
                j = j-1
    return True

def largestPalindrome(n):
    prodList = prodTwo(n)
    result = []
    for num in prodList[::-1]: # the biggest numbers are gathered at the end
        if len(result) > 10: # 10 matches should be good enough to find the max
            break
        elif palindrome(num):
            result.append(num)
    return max(result)

# Test cases
# ----------
print prodTwo(5)
# [1, 2, 3, 4, 5, 4, 6, 8, 10, 9, 12, 15, 16, 20, 25]
print palindrome(54)
# False
print palindrome(454)
# True
print largestPalindrome(99)
# 9009
print largestPalindrome(999)
# 906609