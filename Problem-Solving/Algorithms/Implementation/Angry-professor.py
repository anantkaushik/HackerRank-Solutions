"""
Problem Link - https://www.hackerrank.com/challenges/angry-professor/problem
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present when class starts.
).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.
Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

    k: the threshold number of students
    a: an array of integers representing arrival times

"""
n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for j in a:
        if j<=0:
            count=count+1
    if count<k:
        print("YES")
    else:
        print("NO")