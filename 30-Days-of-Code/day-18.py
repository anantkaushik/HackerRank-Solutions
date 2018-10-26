"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. 
Can you determine if a given string, , is a palindrome?
To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push that same character onto a stack. 
Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two 
characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character 
until our containers are empty (a non-match means s isn't a palindrome).
Write the following declarations and implementations:
Two instance variables: one for your stack, and one for your queue.
1. A void pushCharacter(char ch) method that pushes a character onto a stack.
2. A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
3. A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
4. A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.

Input Format
You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string s. 
It then calls the methods specified above to pass each character to your instance variables.

Constraints
s is composed of lowercase English letters.

Output Format
You are not responsible for printing any output to stdout.
If your code is correctly written and s is a palindrome, the locked stub code will print The word, s, is a palindrome.; 
otherwise, it will print The word, s, is not a palindrome.

Sample Input
racecar

Sample Output
The word, racecar, is a palindrome.
"""
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    def pushCharacter(self,x):
        self.stack.append(x)
    def enqueueCharacter(self,x):
        self.queue.append(x)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")