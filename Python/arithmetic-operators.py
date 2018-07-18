"""
Task 
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format
The first line contains the first integer,a. The second line contains the second integer,b.

Output Format
Print the three lines as explained above.

Sample Input:
3
2

Sample Output:
5
1
6

Explanation:
3 + 2 = 5
3 - 2 = 1
3 * 2 = 6
"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)