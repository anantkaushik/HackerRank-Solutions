"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art 
based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format
Only one line of input containing N, the size of the rangoli.

Output Format
Print the alphabet rangoli in the format explained above.

Sample Input
5

Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string
def print_rangoli(size):
    a = string.ascii_lowercase
    r = []
    for i in range(size):
        s = "-".join(a[i:size])
        r.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(r[:0:-1]+r))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)