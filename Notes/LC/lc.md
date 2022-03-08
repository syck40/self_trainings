################################
Toolbox
1. create a subfunction to recurse
2. keep a tree level as a tuple in a list

################################



# https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

- store a tuple of (node, level)

# https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

- recursive dfs, handle all False cases as base case

# https://leetcode.com/problems/invert-binary-tree/
- recursive dfs, preorder do work(swapping), then go on to recur left and then right

# https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
- keep a tuple of levels and do BFS

# https://leetcode.com/problems/subtree-of-another-tree/
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

- DFS/BFS each node subfunction to check if same
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _tree_check(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return _tree_check(r1.left, r2.left) and _tree_check(r1.right, r2.right)
            
        ss = [root]
        while ss:
            val = ss.pop()
            ret = _tree_check(val,subRoot)
            if ret:
                print(ret)
                return True
            if val.left:
                ss.append(val.left)
            if val.right:
                ss.append(val.right)
        return False

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

- common ancestor means they need to be on the same side of the root
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < root.val and q.val < root.val:
                curr = root.left
            elif p.val > root.val and q.val > root.val:
                curr = root.right
            else:
                return curr

# https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

- 
