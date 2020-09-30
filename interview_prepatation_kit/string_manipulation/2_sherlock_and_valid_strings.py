#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the isValid function below.

def isVal(s):    
    d=defaultdict(int)
    for i in s:
        d[i]+=1
    a=[]
    for i in d.keys():
        a.append(d[i])    
    return len(set(a)) == 1

def isValid(s):
    d=defaultdict(int)
    for i in s:
        d[i]+=1
    print(d)        
    count_of_one=0
    one=None
    maxx = 0
    maxxChar=None
    for i in d.keys():
        if maxx < d[i]:
            maxx=d[i]
            maxxChar=i
        if d[i] == 1:
            count_of_one+=1
            one=i 
    if count_of_one > 1:
        return "NO"
    if not isVal(s):
        if one!=None:
            b=s[:]   
            b = b[:b.find(one)]+b[b.find(one)+1:]
            if isVal(b):
                return "YES"
        b=s[:]
        b = b[:b.find(maxxChar)]+b[b.find(maxxChar)+1:]
        if isVal(b):
            return "YES"
        return "NO"
    else: 
        return "YES"              


                                 
   
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
