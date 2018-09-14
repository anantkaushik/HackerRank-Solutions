"""
Problem Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 
for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet a = (a[0],a[1],a[2]), and the rating for Bob's challenge to be the triplet 
b = (b[0],b[1],b[2]).
Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1],and a[2] with b[2].

If a[i] > b[i] ,then Alice is awarded  point.
If a[i] < b[i] ,then Bob is awarded  point.
If a[i] = b[i] ,then neither person receives a point.

Comparison points is the total points a person earned.
Given a and b, determine their respective comparison points.

Function Description
Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score 
and the second being Bob's.
compareTriplets has the following parameter(s):
a: an array of integers representing Alice's challenge rating
b: an array of integers representing Bob's challenge rating

Input Format
The first line contains 3 space-separated integers a[0], a[1] and, a[2] describing the respective values in triplet a.
The second line contains 3 space-separated integers b[0], b[1] and, b[2] describing the respective values in triplet b. 

Output Format
Return an array of two integers denoting the respective comparison points earned by Alice and Bob.

Sample Input 0
5 6 7
3 6 10

Sample Output 0
1 1

Sample Input 1
17 28 30
99 16 8

Sample Output 1
2 1
"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice,bob =0,0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice,bob] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()