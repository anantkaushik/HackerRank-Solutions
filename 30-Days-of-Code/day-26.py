"""
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program 
that calculates the fine (if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same calendar month and year as the 
expected return date, fine = 15 Hackos * no. of days late.
If the book is returned after the expected return month but still within the same calendar year as the expected 
return date, the fine = 500 Hackos * no. of months late.
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format
The first line contains space-separated integers denoting the respective day, month, and year on which the book was 
actually returned.
The second line contains space-separated integers denoting the respective day, month and year on which the book was 
expected to be returned (due date).

Constraints
1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000
It is guaranteed that dates will be valid Gregorian Calendar dates.

Output Format
Print a single integer denoting the library fine for the book received as input.

Sample Input
9 6 2015
6 6 2015
Sample Output
45
"""
returnDate = list(map(int, input().split()))
dueDate = list(map(int, input().split()))

fine = 0
if returnDate[2] > dueDate[2]:
    fine = 10000
elif returnDate[2] == dueDate[2]:
    if returnDate[1] > dueDate[1]:
        fine = 500 * (returnDate[1] - dueDate[1])
    elif returnDate[1] == dueDate[1]:
        if returnDate[0] > dueDate[0]:
            fine = 15 * (returnDate[0] - dueDate[0])

print(fine)