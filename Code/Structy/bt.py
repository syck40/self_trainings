"""
    a
   / \
  b
root, leaf(no child), parent child

bst
every node at most 2 children
bst, only 1 way get from 1 node to another
1 root
[a]
[a] [c, b]
[b] [c,e,d]
[d] [c,e]
[e] [c,g]
[g] [c]
[c] [f]
3 11 4 -2 4 1

3 -> 3
4, 11 -> 11
4, -2, 4 -> 4
4, -2 -> -2
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
a.left = b
a.right = c
