"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

Input Format
A single line of input consisting of the string S.

Output Format
A single line of output consisting of the modified string.

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
"""
from itertools import groupby
s = input()
print(*[(len(list(g)),int(k)) for k, g in groupby(s)])