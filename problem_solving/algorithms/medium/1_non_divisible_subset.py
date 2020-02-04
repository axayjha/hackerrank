"""
    https://www.hackerrank.com/challenges/non-divisible-subset/problem

    Given a set of distinct integers, print the size of a maximal subset of S 
    where the sum of any 2 numbers in S' is not evenly divisible by k.

    For example, the array s=[19, 10, 20, 10, 24, 25, 22] and k=4.
    One of the arrays that can be created is s'[0] = [10, 12, 25]. Another is s'[1]=[19, 22, 24]. 
    After testing all permutations, the maximum length solution array has 3 elements.


    Max Score = 20
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    d = defaultdict(list)
    s_modded = [0]*len(s)
    c = 0
    for i in range(len(s)):
        s_modded[i] = s[i]%k 
        d[s_modded[i]].append(s[i])
    if len(d[0]) > 0:
        c += 1
    print(d)        
    for i in range(1, k//2+1):
        j = k - i 
        if i!=j:
            if len(d[i]) > len(d[j]):
                c += len(d[i])
            else:
                c += len(d[j])
        else:
            if len(d[i]) > 0:
                c += 1
    return c          


# s=[19, 10, 20, 10, 24, 25, 22]
# k=4

# s=[1, 7, 2, 4]
# k = 3

s=[278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k=7

print(nonDivisibleSubset(k, s))