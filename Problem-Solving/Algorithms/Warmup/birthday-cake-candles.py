"""
Problem Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

You are in charge of the cake for your niece's birthday and have decided the cake will have one 
candle for each year of her total age. When she blows out the candles, she’ll only be able to 
blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.


For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3, 
she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and 
there are 2 such candles.

Function Description
Complete the function birthdayCakeCandles in the editor below. It must return an integer 
representing the number of candles she can blow out.
birthdayCakeCandles has the following parameter(s):
ar: an array of integers representing candle heights

Input Format
The first line contains a single integer, n, denoting the number of candles on the cake. 
The second line contains n space-separated integers, where each integer i describes 
the height of candle i.

Output Format
Return the number of candles that can be blown out on a new line.

Sample Input 0
4
3 2 1 3

Sample Output 0
2
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen
    highest_candle = count = 0
    for c in ar:
        if c > highest_candle:
            highest_candle = c
            count = 1
        elif c == highest_candle:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()