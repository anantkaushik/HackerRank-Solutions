"""
You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer n followed by the names and marks for students. 
You are required to save the record in a dictionary data type. The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format:
The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by that student 
separated by a space. The final line contains the name of a particular student previously listed.

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output:
26.50
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    summ = sum(student_marks[query_name])
    print("%.2f" % (summ/3))