"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
"""
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def addtwo(l1,l2):
    num = l1[-1::-1]
    num2 = l2[-1::-1]
    nn = ""
    nn2 = ""
    for i in num:
        nn += str(i)

    for i in num2:
        nn2 += str(i)
    ret = str(int(nn) + int(nn2))
    ret2 = []
    for i in ret[-1::-1]:
        ret2.append(int(i))

    print(ret2)
addtwo(l1,l2)
