"""
Task:
Given an integer,n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input
3
Sample Output
Weird

Sample Input
24
Sample Output
Not Weird
"""
if __name__ == '__main__':
    N = int(input())
    if (N % 2 != 0) or (N%2 == 0 and N >= 6 and N <= 20):
        print("Weird")
    else:
        print("Not Weird")
