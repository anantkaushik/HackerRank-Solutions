"""
Problem Link: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

Given pointers to the head nodes of 2 linked lists that merge together at some point, find the Node where the two 
lists merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.
In the diagram below, the two lists converge at Node x:
[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q
Complete the int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) method so that it finds
and returns the data value of the Node where the two lists merge.

Input Format
Do not read any input from stdin/console.
The findMergeNode(SinglyLinkedListNode,SinglyLinkedListNode) method has two parameters, head1 and head2, 
which are the non-null head Nodes of two separate linked lists that are guaranteed to converge.

Output Format
Do not write any output to stdout/console.
Each Node has a data field containing an integer. Return the integer data for the Node where the two lists merge.

Sample Input
The diagrams below are graphical representations of the lists that input Nodes headA and headB are connected to. 
Recall that this is a method-only challenge; the method only has initial visibility to those 2 Nodes and 
must explore the rest of the Nodes using some algorithm of your own design.

Test Case 0
 1
  \
   2--->3--->NULL
  /
 1

Test Case 1
1--->2
      \
       3--->Null
      /
     1

Sample Output
2
3

Explanation
Test Case 0: As demonstrated in the diagram above, the merge Node's data field contains the integer 2. 
Test Case 1: As demonstrated in the diagram above, the merge Node's data field contains the integer 3.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
 
# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    slow = head1
    fast = head2
    while slow != fast:
        slow = slow.next if slow.next else head2
        fast = fast.next if fast.next else head1
    return slow.data
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()