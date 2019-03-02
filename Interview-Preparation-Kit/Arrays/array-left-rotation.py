"""
Problem Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
Given an array a of n integers and a number, d, perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers. 

Function Description
Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):
An array of integers a.
An integer d, the number of rotations.

Input Format
The first line contains two space-separated integers n and d, the size of a and the number of left rotations 
you must perform. 
The second line contains n space-separated integers a[i].

Output Format
Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(nums, k):
    k = k % len(nums)
    count = start = len(nums)-1
    while count >=0 :
        cur = start
        prev = nums[start]
        while 1:
            nextt = (cur - k) % len(nums)
            nums[nextt], prev = prev, nums[nextt]
            cur  = nextt
            count -= 1
            if start == cur:
                break
        start -= 1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()