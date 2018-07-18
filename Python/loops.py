"""
Task 
Read an integer n. For all non-negative integers i < n, print i*i. See the sample for details.

Input Format
The first and only line contains the integer, n.

Output Format
Print n lines, one corresponding to each i.

Sample Input:
5

Sample Output:
0
1
4
9
16
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)