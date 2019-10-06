"""
PROBLEM LINK - https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

    n: the integer length of array ar
    ar: an array of integers
    k: the integer to divide the pair sum by 

Sample Input:-
6 3
1 3 2 6 1 2
Sample Output:-
5
"""
n,k=map(int,input().split())
li=list(map(int,input().split()))
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if (li[i]+li[j])%k==0:
            count=count+1
print(count)
