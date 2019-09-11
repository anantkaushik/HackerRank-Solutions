"""
Problem Link: https://www.hackerrank.com/challenges/find-digits/problem

An integer d is a divisor of an integer n if the remainder of n/d = 0.
Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer.

Function Description
Complete the findDigits function in the editor below. It should return an integer representing the number of digits of d 
that are divisors of d.
findDigits has the following parameter(s):
n: an integer to analyze

Input Format
The first line is an integer, t, indicating the number of test cases.
The t subsequent lines each contain an integer, n.

Output Format
For every test case, count the number of digits in n that are divisors of n. Print each answer on a new line.

Sample Input
2
12
1012

Sample Output
2
3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while temp:
        if temp % 10 > 0:
            count += 1 if not n%(temp%10) else 0
        temp //= 10
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
