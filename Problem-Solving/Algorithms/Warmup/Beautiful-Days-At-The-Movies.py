"""
Problem Link - https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

Function Description

Complete the beautifulDays function in the editor below. It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):

    i: the starting day number
    j: the ending day number
    k: the divisor

"""
a, b, k = map(int,input().split())
ans = 0
for i in range(a, b+1):
    ans = ans + abs(not (i - int(str(i)[::-1]))%k)
print(ans)