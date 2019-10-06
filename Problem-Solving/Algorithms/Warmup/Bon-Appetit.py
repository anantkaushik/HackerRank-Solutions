"""
PROBLEM LINK - https://www.hackerrank.com/challenges/bon-appetit/problem

Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. 
You must determine if his calculation is correct.

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

    bill: an array of integers representing the cost of each item ordered
    k: an integer representing the zero-based index of the item Anna doesn't eat
    b: the amount of money that Anna contributed to the bill

"""
ni,adt=input().split()
m1=int(adt)
m2=int(ni)
m=list(map(int,input().split()))
charge=int(input())
sum=0
for i in range(len(m)):
    if i==m1:
        continue
    else:
        sum=sum+m[i]
half=sum//2
if charge==half:
    print("Bon Appetit")
else:
    print(charge-half)
    