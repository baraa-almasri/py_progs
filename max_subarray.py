#!/usr/bin/python3


# crazy bruteforce
def getMaxSubarray(array: list):
    # subarrays set
    subArrays = []
    subArrayIndex = 0
    # sums of the subarrays to get the index of the max subarray
    sums = []

    for k in range(len(array)):
        for l in range(k, len(array)):
            # add chopped off arrays to thier list
            subArrays.append( array[k:l] )
            # add sums to thier list
            sums.append( sum( subArrays[ subArrayIndex ] ) )
            # update subArray index
            subArrayIndex += 1

    if max(sums) >= 0:
        # return the maximum subarray
        return subArrays[sums.index( max(sums) ) ]
    # if the max is not positive
    return []

    return sums
# using divide and conquer
import sys # for numbers limits

def findMaxCrossingSubarray(array: list, low: int, high: int):
    mid = int((low + high) / 2 )

    leftSum = -1 * sys.maxsize # equivalent to -infinity
    maxLeft = 0
    sum = 0
    for i in range(mid, low, -1):
        sum += array[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -1 * sys.maxsize # equivalent to -infinity
    sum = 0
    maxRight = 0
    for j in range(mid + 1, high):
        sum += array[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = i

    return maxLeft, maxRight, (leftSum + rightSum)

from math import floor
def getMaxSubarray2(array: list, low: int, high: int):
    if high == low:
        return low, high, array[low]

    mid = int(floor((low + high) / 2))

    leftLow, leftHigh, leftSum = getMaxSubarray2(array, low, mid)
    rightLow, rightHigh, rightSum  = getMaxSubarray2(array, mid + 1, high)
    crossLow, crossHigh, crossSum  = findMaxCrossingSubarray(array, low, high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return leftLow, leftHigh, leftSum
    elif rightSum >= leftSum and rightSum >= crossSum:
        return rightLow,rightHigh, leftSum
    else:
        return crossLow, crossHigh, crossSum



a = [1,2,3,9,0,-6,-4,3,-3,4,99,4,-90]
print(getMaxSubarray(a))

print(getMaxSubarray2( a, 0, 12 ))
