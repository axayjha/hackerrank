"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

MAX SCORE: 20
"""


#!/bin/python3

import math
import os
import random
import re
import sys
import bisect 

def climbingLeaderboard(scores, alice):
    s = list(sorted(set(scores)))
    
    l = len(s)
    ans=[]
    for i in alice:
        x = bisect.bisect_right(s, i, 0, l)
        ans.append(l+1-x)
    return ans

# implement bisect on your own!

s=[100, 90, 90, 80, 75, 60]
a=[50, 65, 77, 90, 102]

print(climbingLeaderboard2(s, a))


        

