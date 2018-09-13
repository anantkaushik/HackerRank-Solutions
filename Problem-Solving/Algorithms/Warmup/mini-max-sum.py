"""
Problem Link: https://www.hackerrank.com/challenges/mini-max-sum/problem

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Function Description
Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and 
the maximum sum of 4 of 5 elements.
miniMaxSum has the following parameter(s):
arr: an array of 5 integers

Input Format
A single line of five space-separated integers.

Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly 
four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input
1 2 3 4 5

Sample Output
10 14
"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    m = sum(arr)
    print(m-max(arr),m-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
