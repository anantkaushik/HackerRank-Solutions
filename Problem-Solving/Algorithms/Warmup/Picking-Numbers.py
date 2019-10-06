"""
PROBLEM LINK - https://www.hackerrank.com/challenges/picking-numbers/problem
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1.

Function Description

Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.

pickingNumbers has the following parameter(s):

    a: an array of integers
"""
n=int(input())
a=list(map(int,input().split()))
maximum=0
diff=1
for k in a:
    n1=a.count(k)
    n2=a.count(k-diff)
    maximum=max(maximum,n1+n2)
print(maximum)