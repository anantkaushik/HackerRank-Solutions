"""
Problem Sort: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following three lines:
Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.

Function Description
Complete the function countSwaps in the editor below. It should print the three lines required, then return.
countSwaps has the following parameter(s):
a: an array of integers.

Input Format
The first line contains an integer, n, the size of the array a. 
The second line contains n space-separated integers a[i].

Output Format
You must print the following three lines of output:
Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.

Sample Input 0
3
1 2 3

Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Explanation 0 
The array is already sorted, so 0 swaps take place and we print the necessary three lines of output shown above.

Sample Input 1
3
3 2 1

Sample Output 1
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        flag = 0
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
                flag = 1
        if flag == 0:
            break
    print("Array is sorted in",count,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)