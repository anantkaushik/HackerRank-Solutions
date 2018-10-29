"""
Task 
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated 
strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.

Input Format
The first line contains an integer, T (the number of test cases). 
Each line i of the T subsequent lines contain a String, S.

Output Format
For each String S<j> (where 0<=j<=T-1), print S<j>'s even-indexed characters, followed by a space, followed by S<j>'s odd-indexed characters.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak
"""
for _ in range(int(input())):
    s = input()
    print(s[0::2],s[1::2])
