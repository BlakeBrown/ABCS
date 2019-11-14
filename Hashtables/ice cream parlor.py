#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    hashtable = {}
    for index, cost in enumerate(arr):
        if m - cost in hashtable:
            return sorted([index+1, hashtable[m-cost]])
        hashtable[cost] = index+1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
