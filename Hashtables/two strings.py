#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    lookup = set()
    for c in s1:
        lookup.add(c)
    for c in s2:
        if c in lookup:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
