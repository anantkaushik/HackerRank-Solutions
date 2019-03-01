"""
Problem Link: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode object 
having data value data and insert it into a sorted linked list while maintaining the sort.

Function Descriptio
Complete the sortedInsert function in the editor below. It must return a reference to the head of your modified 
DoublyLinkedList.

sortedInsert has two parameters:
head: A reference to the head of a doubly-linked list of DoublyLinkedListNode objects.
data: An integer denoting the value of the data field for the DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where head=NULL) and a list with one element are sorted lists.

Input Format
The first line contains an integer t, the number of test cases.

Each of the test case is in the following format:
The first line contains an integer n, the number of elements in the linked list.
Each of the next n lines contains an integer, the data for each node of the linked list.
The last line contains an integer data which needs to be inserted into the sorted doubly-linked list.

Output Format
Do not print anything to stdout. Your method must return a reference to the head of the same list 
that was passed to it as a parameter.
The ouput is handled by the code in the editor and is as follows: 
For each test case, print the elements of the sorted doubly-linked list separated by spaces on a new line.

Sample Input
1
4
1
3
4
10
5

Sample Output
1 3 4 5 10
"""
#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if data <= head.data:
        node.next = head
        head.prev = node
        head = node
        return head
    cur = head
    while cur.next:
        if cur.next.data > data:
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
            return head
        cur = cur.next
    cur.next = node
    node.prev = cur
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()