# Problem 8
# ---------
'''
The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.
 73167176531330624919225119674426574742355349194934
 96983520312774506326239578318016984801869478851843
 85861560789112949495459501737958331952853208805511
 12540698747158523863050715693290963295227443043557
 66896648950445244523161731856403098711121722383113
 62229893423380308135336276614282806444486645238749
 30358907296290491560440772390713810515859307960866
 70172427121883998797908792274921901699720888093776
 65727333001053367881220235421809751254540594752243
 52584907711670556013604839586446706324415722155397
 53697817977846174064955149290862569321978468622482
 83972241375657056057490261407972968652414535100474
 82166370484403199890008895243450658541227588666881
 16427171479924442928230863465674813919123162824586
 17866458359124566529476545682848912883142607690042
 24219022671055626321111109370544217506941658960408
 07198403850962455444362981230987879927244284909188
 84580156166097919133875499200524063689912560717606
 05886116467109405077541002256983155200055935729725
 71636269561882670428252483600823257530420752963450
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
'''
# put the 1000-digit number in num
num1 = '73167176531330624919225119674426574742355349194934'
num2 = '96983520312774506326239578318016984801869478851843'
num3 = '85861560789112949495459501737958331952853208805511'
num4 = '12540698747158523863050715693290963295227443043557'
num5 = '66896648950445244523161731856403098711121722383113'
num6 = '62229893423380308135336276614282806444486645238749'
num7 = '30358907296290491560440772390713810515859307960866'
num8 = '70172427121883998797908792274921901699720888093776'
num9 = '65727333001053367881220235421809751254540594752243'
num10 = '52584907711670556013604839586446706324415722155397'
num11 = '53697817977846174064955149290862569321978468622482'
num12 = '83972241375657056057490261407972968652414535100474'
num13 = '82166370484403199890008895243450658541227588666881'
num14 = '16427171479924442928230863465674813919123162824586'
num15 = '17866458359124566529476545682848912883142607690042'
num16 = '24219022671055626321111109370544217506941658960408'
num17 = '07198403850962455444362981230987879927244284909188'
num18 = '84580156166097919133875499200524063689912560717606'
num19 = '05886116467109405077541002256983155200055935729725'
num20 = '71636269561882670428252483600823257530420752963450'
num = ''
for i in range(1,21):
    num = num + eval('num'+str(i))

def prodSeries(n):
    # return product of digits in n
    result = 1
    for num in n:
        result = result*int(num)
    return result

def largestProdInSeries(n, k):
    # Find the k adjacent digits in n that have the greatest product
    resultMax = prodSeries(n[0:k])
    for j in range(1,len(n)-k+1):
        result = prodSeries(num[j:j+k])
        resultMax = max(result, resultMax)
    return resultMax

# Test cases
# ----------
print prodSeries('9989')
# 5832
print largestProdInSeries(num, 4)
# 5832
print largestProdInSeries(num, 13)
# 23514624000