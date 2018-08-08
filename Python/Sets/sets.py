"""
Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all 
the plants with distinct heights in her greenhouse.

Formula used:
Average = Sum of distinct heights / Total number of distict heights.

Input Format
The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.

Output Format
Output the average height value on a single line.

Sample Input
10
161 182 161 154 176 170 167 171 170 174

Sample Output
169.375
"""

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)