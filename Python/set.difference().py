"""
Task
Students of District College have a subscription to English and French newspapers. Some students have subscribed to 
only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has 
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only 
English newspapers.

Input Format
The first line contains the number of students who have subscribed to the English newspaper. 
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper. 
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Output Format
Output the total number of students who are subscribed to the English newspaper only.

Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output
4

Explanation
The roll numbers of students who only have English newspaper subscriptions are:
4,5,7 and 9.
Hence, the total is 4 students.
"""
input()
english = set(map(int,input().split()))
input()
french = set(map(int,input().split()))
print(len(english.difference(french)))