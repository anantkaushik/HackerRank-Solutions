"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of 
matching pairs of socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Input Format

The first line contains an integer n, the number of socks represented in at. 
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Output Format
Return the total number of matching pairs of socks that John can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    for i in ar:
        d[i] = d.get(i,0) + 1
    res = 0
    for k,v in d.items():
        res += v//2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()