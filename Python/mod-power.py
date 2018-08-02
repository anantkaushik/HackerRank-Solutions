"""
Task 
You are given three integers: a, b, and m, respectively. Print two lines. 
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format 
The first line contains a, the second line contains b, and the third line contains m.

Sample Input
3
4
5

Sample Output
81
1
"""
a,b,m = int(input()),int(input()),int(input())
print(pow(a,b))
print(pow(a,b,m))