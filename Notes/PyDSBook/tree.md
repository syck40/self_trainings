nodes, parent-child relationship
siblings, external = leaves
ordered tree, meaningful linear order among children of each node
i.e. book chapter
non - ordered = org chart
binary tree is proper or full if each node has either 0 or 2 children 
                                Tree
                    Binary Tree
                Linked Binary Tree





level 0 -> 1 nodes
1 -> 2 2^n level
2 -> 4 
3 -> 8
array tree, if p is left child of position q, then f(p) = 2f(q) + 1
if p is right child f(p) = 2f(q) + 2
preorder:
    do work
    for c in children(p):
        preorder(c)
postorder:
    for c in children(p):
        postorder(c)
    do work
    expression tree uses this
                
                +
    -                       +
5       6               11      12
breathfirst
    create queue
    while q not empty:
        p = q.dequeue
        perform action
        for each c in p:
            q.enqueue(c)
inorder only for binary tree:
    inorder(p):
        if p has left child:
            inorder(lp)
        dowork
        if p has right child:
            inorder(rp)
BinarySearchTree
    store an ordered sequence of elements in binary tree
    at each node, left is smaller than node and right is larger than node
    this sets up to use binary search at each node to find if target exist
Inorder book
                Paper
    Title   Abstract    ChapI       ChapII
                        1.1 1.2     2.1 2.2
EulerTour, combine pre and post
    euler(t,p):
        do pre action
        for c in t.children(p) do
            euler(t, c)
        do post action
