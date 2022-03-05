tree is type of graph
hierachycal relatinship
node root paraent child leaf sibling edge levels subtree path
root level 0
2^L
path: 3 - 4 - 7 - 10
depth of N = # path from root to N
heigh: longest path from N to leaf, heigh of tree = heigh of root
# of edge = # node - 1
- full binary tree
    0  child or 2 child
- complete binary tree
    all levels filled except last level, leaf can have no sibling, left adjusted
- perfect binary tree
    2 child for all and all leaf are same depth or same level
- balanced binary tree
    hight of the left and right may differ at most 1
- degenerate binary tree
    binary tree where EVERY parent node only has 1 child node
BST:
    left < Node < right
    number of nodes = 2^height + 1 - 1, 2^2+1 - 1 = 7, 2 levels has 7 nodes total
    array form: 2i + 1 = left child, 2i + 2 = right child
tree - binary tree - binary search tree - binary heap
max/min heap are binary tree but not binary search tree
root is max or min of subtree
max heap array rebalancing: n = i/2 - 1 if parent < n swap
max heap vs queue allows logN for insertion/deletion instead of O(n)
trie, char in tree
# graph
no direction, no root
directed, undirected
weighted
