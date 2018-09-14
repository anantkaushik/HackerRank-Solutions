"""
Problem Link: https://www.hackerrank.com/challenges/plus-minus/problem

Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
Print the decimal value of each fraction on a new line.

Function Description
Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, 
each on a separate line rounded to six decimals.
plusMinus has the following parameter(s):
arr: an array of integers

Input Format
The first line contains an integer, n, denoting the size of the array. 
The second line contains n space-separated integers describing an array of numbers.

Output Format
You must print the following 3 lines:
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.

Sample Input
6
-4 3 -9 0 4 1

Sample Output
0.500000
0.333333
0.166667
"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos,neg = 0,0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    l = len(arr)
    print("%.6f"%(pos/l))
    print("%.6f"%(neg/l))
    print("%.6f"%((l-(neg+pos))/l))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)