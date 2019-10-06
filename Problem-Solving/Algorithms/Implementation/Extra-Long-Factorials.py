"""
PROBLEM LINK - https://www.hackerrank.com/challenges/extra-long-factorials/problem
Calculate and print the factorial of a given integer.

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

    n: an integer

"""
n=int(input())
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(fact)