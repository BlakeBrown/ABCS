#!/bin/python3

import os
import sys
from heapq import *

def median(minHeap, maxHeap):
    if len(maxHeap) == len(minHeap):
        return '%.1f' % float((minHeap[0] - maxHeap[0])/2)  
    return '%.1f' % float(-maxHeap[0]) 
     
#
# Complete the runningMedian function below.
#
def runningMedian(a):
    #
    # Write your code here.
    #
    minHeap = []
    maxHeap = []
    ans = []
    for e in a:
        heappush(maxHeap, -e)
        heappush(minHeap, -heappop(maxHeap))
        if len(minHeap) > len(maxHeap):
            heappush(maxHeap, -heappop(minHeap))
        ans.append(median(minHeap, maxHeap))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
