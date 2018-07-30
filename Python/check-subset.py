"""
You are given two sets, A and B. 
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format
The first line will contain the number of test cases, T. 
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Output Format
Output True or False for each test case on separate lines.

Sample Input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output

True 
False
False

Explanation

Test Case 01 Explanation

Set A = {1 2 3 5 6} 
Set B = {9 8 5 6 3 2 1 4 7} 
All the elements of set A are elements of set B. 
Hence, set A is a subset of set B.
"""
t = int(input())
while t > 0:
    n = int(input())
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    print(len(a.intersection(b))==n)
    t -= 1