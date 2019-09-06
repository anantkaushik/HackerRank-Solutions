"""
Problem Link: https://www.hackerrank.com/challenges/grading/problem

HackerLand University has the following grading policy:
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to 
the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Given the initial value of grade for each of Sam's n students, write code to automate 
the rounding process.

Function Description
Complete the function gradingStudents in the editor below. It should return an integer 
array consisting of rounded grades.
gradingStudents has the following parameter(s):
grades: an array of integers representing grades before rounding

Input Format
The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer, grades[i], denoting student i's grade.

Output Format
For each grades[i], print the rounded grade on a new line.

Sample Input 0
4
73
67
38
33

Sample Output 0
75
67
40
33
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res = []
    for grade in grades:
        difference = 5 - (grade%5)
        if difference < 3 and grade >= 38:
            res.append(grade+difference)
        else:
            res.append(grade)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()