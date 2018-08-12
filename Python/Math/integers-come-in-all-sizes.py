"""
Task 
Read four numbers a, b, c and d, and print the result of a**b + c**d.

Input Format 
Integers a, b, c and d are given on four separate lines, respectively.

Output Format 
Print the result of a**b + c**d on one line.

Sample Input
9
29
7
27

Sample Output
4710194409608608369201743232  
"""
a,b,c,d = (int(input()) for i in range(4))
print(a**b+c**d)