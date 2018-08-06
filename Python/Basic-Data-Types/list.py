"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer,n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())
    listt = []
    while N > 0:
        q = list(map(str,input().split()))
        if q[0] == "print":
            print(listt)
        elif q[0] == "insert":
            listt.insert(int(q[1]),int(q[2]))
        elif q[0] == "remove":
            listt.remove(int(q[1]))
        elif q[0] == "append":
            listt.append(int(q[1]))
        elif q[0] == "sort":
            listt.sort()
        elif q[0] == "pop":
            listt.pop()
        elif q[0] == "reverse":
            listt.reverse()
        N -= 1