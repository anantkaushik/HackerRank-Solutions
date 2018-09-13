"""
Problem Link: https://www.hackerrank.com/challenges/calendar-module/problem

Task
You are given a date. Your task is to find what the day is on that date.

Input Format
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Output Format
Output the correct day in capital letters.

Sample Input
08 05 2015

Sample Output
WEDNESDAY
"""
import calendar
m,d,y = map(int,input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())