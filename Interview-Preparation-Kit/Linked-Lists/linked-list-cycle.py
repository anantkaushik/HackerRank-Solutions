"""
Problem Link: https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 

Complete the function has_cycle in the editor below. 
It must return a boolean true if the graph contains a cycle, or false.
has_cycle has the following parameter(s):
head: a pointer to a Node object that points to the head of a linked list.
Note: If the list is empty, head will be null.

Input Format
There is no input for this challenge. A random linked list is generated at runtime and passed to your function.

Output Format
If the list contains a cycle, your function must return true. If the list does not contain a cycle, 
it must return false. The binary integer corresponding to the boolean value returned by your 
function is printed to stdout by our hidden code checker.
"""
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False