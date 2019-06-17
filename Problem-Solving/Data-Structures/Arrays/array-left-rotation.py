"""
Problem Link: https://www.hackerrank.com/challenges/array-left-rotation/problem

A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array, 
[1,2,3,4,5] then the array would become [3,4,5,1,2].

Given an array of n integers and a number, d, perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format
The first line contains two space-separated integers denoting the respective values of n (the number of integers) and d (the number of left rotations 
you must perform). 
The second line contains n space-separated integers describing the respective elements of the array's initial state.

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
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(*rotLeft(a,d))