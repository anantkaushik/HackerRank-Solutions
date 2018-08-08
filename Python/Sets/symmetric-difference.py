"""
Task 
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format
The first line of input contains an integer, M. 
The second line contains M space-separated integers. 
The third line contains an integer, N. 
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input
4
2 4 5 9
4
2 4 11 12

Sample Output
5
9
11
12
"""
input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
a_d = a.difference(b)
b_d = b.difference(a)
for i in b_d:
    a_d.add(i)
for i in sorted(a_d):
    print(i)