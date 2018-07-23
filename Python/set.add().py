"""
Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number 
of distinct country stamps in her collection. She asked for your help. You pick the 
stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.

Input Format
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from. 

Output Format
Output the total number of distinct country stamps on a single line.

Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5

Explanation
UK and France repeat twice. Hence, the total number of distinct country stamps is 5(five).
"""
n = int(input())
stamps = set()
while n > 0:
    stamps.add(input())
    n -= 1
print(len(stamps))