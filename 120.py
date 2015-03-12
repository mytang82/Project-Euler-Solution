# Problem 120
# -----------
'''
Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.
For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49.
And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
'''
'''
n=1:  2a
n=2:  2a^2 + 2 
n=3:  2a^3 + 6a
n=4:  2a^4 + 12a^2 + 2
n=5:  2a^5 + 20a^3 + 10a
n=6:  2a^6 + 30a^4 + 30a^2 + 2
n=7:  2a^7 + 42a^5 + 70a^3 + 14a
n=8:  2a^8 + 56a^6 + 14a^4 + 56a^2 + 2
.
.
.
n=odd:  r=2n*a
n=even:  r=2
Thus, rmax is when n is less than a/2 and ~a/2
'''
rmaxSum = 0
for a in range(3, 1001):
    if a%2 == 0: # a even
        rmax = ((a/2)-1)*2*a
    else: # a odd
        rmax = (a/2)*2*a
    rmaxSum = rmaxSum + rmax
print rmaxSum
# 333082500
