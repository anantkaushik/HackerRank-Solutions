"""
Problem Link: https://www.hackerrank.com/challenges/arrays-ds/problem

Given an array, A, of  N integers, print each element in reverse order as a single line of space-separated integers.

Input Format
The first line contains an integer, N (the number of integers in A). 
The second line contains number space-separated integers describing A.

Output Format
Print all N integers in A in reverse order as a single line of space-separated integers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()