"""
Task 
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input:
3

Sample Output:
Weird

Explanation:
n = 3
n is odd and odd numbers are weird, so we print Weird.

Sample Input:
24

Sample Output:
Not Weird

Explanation: 
n= 24
n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.
"""
N = int(input())
if N % 2 != 0:
    print("Weird")
else:
    if N >= 6 and N <= 20:
        print("Weird")
    else:
        print("Not Weird")