#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    hashtable = defaultdict(int)
    answer = 0
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            stringValue = 1
            for character in s[i:j]:
                modifiedAsciiValue = ord(character) - 97
                stringValue *= primes[modifiedAsciiValue]
            if stringValue in hashtable:
                answer += hashtable[stringValue]
            hashtable[stringValue] += 1
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
