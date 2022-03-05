"""
insertion O(1), only need to pass the head node of the ll which becomes
the current, current.next
"""

class Node:
    def __init__(self, val):
        self._val = val
        self._next = None

ab = Node(5)
ab._next = Node(6)
ab._next._next = Node(7)

def print_list(head):
    curr = head
    print(curr._val)
    if curr._next:
        print_list(curr._next)


print_list(ab)
