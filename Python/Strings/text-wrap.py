"""
You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Input Format
The first line contains a string, S. 
The second line contains the width, w.

Output Format
Print the text wrapped paragraph.

Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)