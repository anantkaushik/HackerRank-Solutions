"""
Problem Link: https://www.hackerrank.com/challenges/time-conversion/problem

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description
Complete the timeConversion function in the editor below. It should return a new string 
representing the input time in 24 hour format.
timeConversion has the following parameter(s):
s: a string representing time in 12 hour format

Input Format
A single string s containing a time in 12-hour clock format.

Output Format
Convert and print the given time in 24-hour format.

Sample Input 0
07:05:45PM

Sample Output
9:05:45
"""
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time_type = s[-2:]
    time = s[:-2].split(":")
    if time_type == "AM":
        if time[0] == "12":
            time[0] = "00"
            return ":".join(time)
        return s[:-2]
    else:
        if time[0] == "12":
            return s[:-2]
        time = s[:-2].split(":")
        time[0] = str(int(time[0])+12)
        return ":".join(time)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()