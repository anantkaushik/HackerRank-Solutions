"""
Problem Link - https://www.hackerrank.com/challenges/library-fine/problem

Function Description

Complete the libraryFine function in the editor below. It must return an integer representing the fine due.

libraryFine has the following parameter(s):

    d1, m1, y1: returned date day, month and year
    d2, m2, y2: due date day, month and year

"""
#!/bin/python3
d1 = list(map(int,input().split()))
d2 = list(map(int,input().split()))
if(d1[2]>d2[2]):
    print("10000")
elif(d1[2]<d2[2]):
    print("0")
elif(d1[1]>d2[1]):
    print(500*abs(d1[1]-d2[1]))
elif(d1[1]<d2[1]):
    print("0")
elif(d1[0]>d2[0]):
    print(15*abs(d1[0]-d2[0]))
else:
    print("0")
