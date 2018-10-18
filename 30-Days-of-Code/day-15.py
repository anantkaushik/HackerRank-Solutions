"""
Task 

Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and 
inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.
Note: If the  argument passed to the insert function is null, then the initial list is empty.

Input Format
The insert function has 2 parameters: a pointer to a Node named head, and an integer value, data. 
The constructor for Node has 1 parameter: an integer value for the data field.
You do not need to read anything from stdin.

Output Format
Your insert function should return a reference to the head node of the linked list.

Sample Input
The following input is handled for you by the locked code in the editor: The first line contains T, the number of test cases. 
The T subsequent lines of test cases each contain an integer to be inserted at the list's tail.
4
2
3
4
1

Sample Output
The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:
2 3 4 1
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        if head == None:
            head = Node(data)
        else:
            cur = head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  