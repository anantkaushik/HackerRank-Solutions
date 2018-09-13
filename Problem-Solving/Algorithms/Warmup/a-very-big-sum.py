"""
Problem Link: https://www.hackerrank.com/challenges/a-very-big-sum/Problem

Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
aVeryBigSum has the following parameter(s):
ar: an array of integers .

Input Format

The first line of the input consists of an integer n. 
The next line contains n space-separated integers contained in the array.

Output Format
Print the integer sum of the elements in the array.

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015
"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    # return sum(ar)  Using Inbuilt function
    summ = 0
    for i in ar:
        summ += i
    return summ # Without using inbuilt function.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
