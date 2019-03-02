"""
Problem Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are 
thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to 
the number of the current cloud plus 1 or 2. She must avoid the thunderheads. Determine the minimum number 
of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

Function Description

Complete the jumpingOnClouds function in the editor below. 
It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):
c: an array of binary integers

Input Format
The first line contains an integer n, the total number of clouds. The second line contains n space-separated 
binary integers describing clouds c[i] where 0<=i<n.

Output Format
Print the minimum number of jumps needed to win the game.

Sample Input 0
7
0 0 1 0 0 1 0

Sample Output 0
4
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = -1
    i = 0
    while i < len(c):
        if i < len(c) - 2 and c[i+2] == 0:
            i += 1
        jump += 1
        i += 1
    return jump
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()