"""
Problem Link: https://www.hackerrank.com/challenges/repeated-string/problem

Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

Function Description
Complete the repeatedString function in the editor below. It should return an integer representing 
the number of occurrences of a in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider

Input Format
The first line contains a single string, s. 
The second line contains an integer, n.

Output Format
Print a single integer denoting the number of letter a's in the first n letters of the infinite string 
created by repeating s infinitely many times.

Sample Input 0
aba
10
Sample Output 0
7

Sample Input 1
a
1000000000000
Sample Output 1
1000000000000
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    count = 0
    for i in s:
        if i == "a":
            count += 1
    if count == 0:
        return 0
    res = count * (n//l)
    for i in range(n%l):
        if s[i] == "a":
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()