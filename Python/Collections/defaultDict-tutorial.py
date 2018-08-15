"""
In this challenge, you will be given 2 integers, n and m.  There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each  words, check whether the word has 
appeared in group A or not. Print the indices of each occurrence of m in group A. 
If it does not appear, print -1.

Input Format
The first line contains integers, n and m separated by a space. 
The next n lines contains the words belonging to group A. 
The next m lines contains the words belonging to group B.

Output Format
Output m lines. 
The ith line should contain the 1-indexed positions of the occurrences of the ith word 
separated by spaces.

Sample Input
5 2
a
a
b
a
b
a
b

Sample Output
1 2 4
3 5
"""
from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(1,n+1):
    d[input()].append(i)
for i in range(m):
    temp = input()
    if temp in d:
        print(*d[temp]) 
    else: 
        print(-1)