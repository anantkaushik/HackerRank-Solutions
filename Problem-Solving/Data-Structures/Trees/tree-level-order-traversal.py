"""
Problem Link: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree. 
In level order traversal, we visit the nodes level by level from left to right. You only have to complete the function. 
For example:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.

Input Format
You are given a function,
void levelOrder(Node * root) {

}

Output Format
Print the values in a single line separated by a space.

Sample Input
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

Sample Output
1 2 5 3 6 4

Explanation
We need to print the nodes level by level. We process each level from left to right. 
Level Order Traversal: 1 -> 2 -> 5 -> 3 -> 6 -> 4.
"""
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    level = [root]
    while level:
        temp = level.pop(0)
        print(temp.info,end=' ')
        if temp.left:
            level.append(temp.left)
        if temp.right:
            level.append(temp.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)