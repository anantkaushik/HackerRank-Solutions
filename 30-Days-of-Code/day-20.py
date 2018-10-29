"""
Task
Given an array, a, of size n containing distinct elements a[0], a[1],..., a[n -1], sort array a in ascending order using the Bubble Sort 
algorithm above. Once sorted, print the following lines:
1. Array is sorted in numSwaps swaps
  where numSwaps is the number of swaps that took place.
2. First Element: firstElement
  where firstElement is the first element in the sorted array.
3. Last Element: lastElement
  where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format
The first line contains an integer, n, denoting the number of elements in array a.
The second line contains n space-separated integers describing a, where the ith integer is a[i], i belongs to [0, n - 1].

Constraints
2 <= n <= 600
1 <= a[i] <= 2 x 10 6, i belongs to [0, n - 1].

Output Format
There should be lines of output:
Array is sorted in numSwaps swaps
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.

Sample Input 0
3
1 2 3

Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Sample Input 1
3
3 2 1

Sample Output 1
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
"""
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalSwap = 0
for i in range(len(a)-1):
    flag = False
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            totalSwap += 1
            flag = True
    if flag == False:
        break
print("Array is sorted in "+str(totalSwap)+" swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])