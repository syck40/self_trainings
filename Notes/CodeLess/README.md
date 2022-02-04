# DS
- 3 types of algo
    - dividing and conquer

    - greedy
        - traveling salesman, take shortest path at each step
    - dynamic
        - make decision catering for future while considering the past
        - looks at multiple solutions, computes them, stores them and recall for reuse
        - greedy approximates, dynamic optimizes
- Linear Data Structures
    - elements are comprised are arranged in such manner that they are ordered sequentially
    - list -> singly -> double -> circular -> buffer or queues
    - priority queues: uses a k/v to arrange the items.  Every item has a priority associated with it and can be thought of as a key.  Higher priority will be dequeued, same priority will be dequeued according to order within the queue.
- Non-linear
    - Trees
        - root, parent, child, leaf, edge
        - binary tree: each parent can be two child or less
        - bst, sorted, all nodes are greater than the nodes in their left subtree, smaller than right.  Smallest is at the end of leftmost subtree
        - unbalanced = nodes only have 1 child.  Balancing tree -> make tree have minimum height.
        - avl binary, detects a heigh diff between two child subtrees it performce tree rotation that moves 1 node of the tree up and the other down.
        - red-black tree also performs self-balancing
        - b-tree, parent can have more than 2 children like filesystem
        - heaps are type of tree, useful for quick access to max and min nodes within a tree.  Uses priority queue
    - Graphs
        - Graph is tree with no root, graph has no nodes can be identified as parent/child
        - weighted graph, edges with weight

# Algo
- Search
    - linear search O(n)
    - binary search
- Sorting
    - bubble sort
    l1 = [10, 18, 6, 2, 4, 16, 8, 14, 12]
    def replace(left, right):
        if right < left:
            tmp = left
            left = right
            right = tmp

    for j in range(len(l1)-1):
        for i in range(len(l1), 0, -1):
            replace(l1[i-1], l1[i])

    - merge sort
    len(l1) #9, l1[0] -> l1[8]
    def divide(l1):
        if len(l1) == 1:
            return l1
        
        mid = len(l1) // 2
        left = l1[:mid]
        right = l1[mid:]
        small_left = divide(left)
        small_right = divide(right)
        if small_left[0] < small_right[0]:
            ret = small_left + small_right
        else:
            ret = small_right + small_left

        return ret
    - O(NlogN)
    - quick sort
    [6, 10, 16, 2, 4, 18, 8, 14, 12]
    pivot = 4, left_marker = 6, right_marker = 12
