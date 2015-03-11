# Problem 2
# ---------
'''
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''

def fibSeq(maxValue):
    ''' generate fibList up to maxValue '''
    fibList = [1,1] # corresponds to n=1 and n=2 case
    # while loop when fibList has not reached maxValue
    while maxValue > fibList[-1]:
        fibList.append(fibList[-1] + fibList[-2])
    return fibList[:-1] # remove the last term that is larger than maxValue
def fibSeqEvenValueSum(maxValue):
    fibList = fibSeq(maxValue)
    result = 0
    for i in range(len(fibList)):
        if fibList[i]%2 == 0:
            result = result + fibList[i]
    return result

# Test cases
# ----------
print fibSeqEvenValueSum(4e6)
# 4613732