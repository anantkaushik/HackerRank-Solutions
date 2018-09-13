"""
Problem Link: https://www.hackerrank.com/challenges/simple-array-sum/problem

Given an array of integers, find the sum of its elements.

Function Description
Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
simpleArraySum has the following parameter(s):
ar: an array of integers

Input Format
The first line contains an integer, n, denoting the size of the array. 
The second line contains n space-separated integers representing the array's elements.

Output Format
Print the sum of the array's elements as a single integer.

Sample Input
6
1 2 3 4 10 11

Sample Output
31
"""
#!/bin/python3
import os
import sys

# Complete the simpleArraySum function below.
def simpleArraySum(ar):
    # return sum(ar)  Using Inbuilt function
    summ = 0
    for i in ar:
        summ += i
    return summ # Without using inbuilt function.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
