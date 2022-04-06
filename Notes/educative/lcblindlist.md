- [1. Blind list sorted by importance](#1-blind-list-sorted-by-importance)
  - [1.1. Clone Graph](#11-clone-graph)
  - [1.2. Coin Change](#12-coin-change)
  - [1.3. Target Sum](#13-target-sum)
  - [1.4. Kth Smallest Element in a BST](#14-kth-smallest-element-in-a-bst)
  - [1.5. Course Schedule](#15-course-schedule)
  - [1.6. Course Schedule II](#16-course-schedule-ii)
  - [1.7. All nodes distance K in Binary Tree](#17-all-nodes-distance-k-in-binary-tree)
  - [1.8. Path Sum II](#18-path-sum-ii)
  - [1.9. Path Sum III](#19-path-sum-iii)
  - [1.10. Maximum Product Subarray](#110-maximum-product-subarray)
  - [1.11. Longest Increasing Subsequence](#111-longest-increasing-subsequence)
  - [1.12. Longest Common Subsequence](#112-longest-common-subsequence)
  - [1.13. House Robber](#113-house-robber)
  - [1.14. Word Search](#114-word-search)
  - [1.15. 0/1 Knapsack](#115-01-knapsack)
  - [1.16. Valid parentheses](#116-valid-parentheses)
  - [1.17. LRU cache](#117-lru-cache)
- [2. Solutions](#2-solutions)
  - [2.1. Clone Graph](#21-clone-graph)
  - [2.2. Coin Change](#22-coin-change)
  - [2.3. Target Sum](#23-target-sum)
  - [2.4. Kth Smallest Element in a BST](#24-kth-smallest-element-in-a-bst)
  - [2.5. Course Schedule](#25-course-schedule)
  - [2.6. Course Schedule II](#26-course-schedule-ii)
  - [2.7. All nodes distance K in Binary Tree](#27-all-nodes-distance-k-in-binary-tree)
  - [2.8. Path Sum II](#28-path-sum-ii)
  - [2.9. Path Sum III](#29-path-sum-iii)
  - [2.10. Maximum Product Subarray](#210-maximum-product-subarray)
  - [2.11. Longest Increasing Subsequence](#211-longest-increasing-subsequence)
  - [2.12. Longest Common Subsequence](#212-longest-common-subsequence)
  - [2.13. House Robber](#213-house-robber)
  - [2.14. Word Search](#214-word-search)
  - [2.15. 0/1 Knapsack](#215-01-knapsack)
  - [2.16. Valid parentheses](#216-valid-parentheses)
  - [2.17. LRU cache](#217-lru-cache)

# 1. Blind list sorted by importance
## 1.1. Clone Graph
   - Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]] 
Output: [[2,4],[1,3],[2,4],[1,3]]
```
   - https://leetcode.com/problems/clone-graph/

## 1.2. Coin Change
   - You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.
   - https://leetcode.com/problems/coin-change/
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```
## 1.3. Target Sum
   - You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.
    - https://leetcode.com/problems/target-sum/
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
``` 
## 1.4. Kth Smallest Element in a BST
  - Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
  - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
  - https://www.youtube.com/watch?v=5LUXSvjmGCw&feature=youtu.be
  - BST think sorted
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## 1.5. Course Schedule
- There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
- https://leetcode.com/problems/course-schedule/
- Adjacency list or a premap to keep track of dependency
- DFS on adjacnecy list
- visited set
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```
## 1.6. Course Schedule II
- There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
```
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```
- 
## 1.7. All nodes distance K in Binary Tree
- Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```
## 1.8. Path Sum II
- Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```
## 1.9. Path Sum III
- Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
```
Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```
## 1.10. Maximum Product Subarray
- Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
## 1.11. Longest Increasing Subsequence
- https://leetcode.com/problems/longest-increasing-subsequence/
- Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```
## 1.12. Longest Common Subsequence
- https://leetcode.com/problems/longest-common-subsequence/
- 2d grid for dp
## 1.13. House Robber
- https://leetcode.com/problems/house-robber/
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
## 1.14. Word Search
- https://leetcode.com/problems/word-search/
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```
## 1.15. 0/1 Knapsack
- Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an item in the knapsack or skip it.
- Similar problems:
  - Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
  - Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
  - Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

## 1.16. Valid parentheses
- https://leetcode.com/problems/valid-parentheses/
```
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
```
- Think open brackets can be added with no regard, but valid checks need to be enforced on closing bracket.

## 1.17. LRU cache
- https://leetcode.com/problems/lru-cache/
- doublely linked list nodes, hashmap map key to LL node
- Node class has a k/v, prev and next pointer
- Cache class has cap, cache dict, left and right pointing to dummy Node class
- Put first check if key in cache, if so remove it from cache then set to new Node(value)
- Removal opt for a doubly linked list, storing the prev and next of current node, them set prev.next = curr.next, nxt.prev = curr.prev
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />


# 2. Solutions
## 2.1. Clone Graph
```
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # keep hash of old:new
        visited = {}
        def _dfs(node):
            if not node:
                return
            new_node = Node(node.val)
            visited[node] = new_node
            for nei in node.neighbors:
                # foreach old neighbors check if exist to prevent cyclic
                if nei not in visited:
                    # foreach old neighbors, recurs to make new ones
                    _dfs(nei)
                    # at the end of new neighbors created, add them to the root new one
                new_node.neighbors.append(visited[nei])
            return new_node
        return _dfs(node)
```
## 2.2. Coin Change
```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _recurs(n, tar):
            # make default val super large
            min_coins = float('inf')
            if tar == 0:
                return 0
            if tar < 0:
                # void this run by setting it to super large
                return min_coins
            for coin in n:
                # choose leave or take
                print(tar, coin)
                min_coins = min(min_coins, 1 + _recurs(coins, tar - coin))
                print(f'res {min_coins}')
            return min_coins
        return _recurs(coins, amount)
```
## 2.3. Target Sum
```
def ss(n, tar):
    def _recur(n, tar, curr):
    # set initial counter to 0, check cursor is less than len()
        counter = 0
        if curr >= len(n):
            return counter
        if curr == len(n) - 1:
            if n[curr] == tar or n[curr] == -tar:
                counter += 1
        
        counter += _recur(n, tar - n[curr], curr + 1)
        counter += _recur(n, tar + n[curr], curr + 1)
        return counter
    # starts with 0 index and target value
    return(_recur(n, tar, 0))

print(ss([1,1,1,1,1],3))
```
with Memo
```
def ss(n, t, memo):
    def _recur(n,t,cur,memo):
        counter = 0
        # base cases
        max_length = len(n)
        if cur >= max_length:
            return counter
        # memo
        if (cur, t) in memo:
            return memo[(cur, t)]

        # increment block
        if cur == max_length - 1:
            if t == n[cur]:
                counter += 1
            if t == -n[cur]:
                counter += 1
        # advancing block
        counter += _recur(n, t - n[cur], cur + 1, memo)
        counter += _recur(n, t + n[cur], cur + 1, memo)
        memo[(cur, t)] = counter

        print(memo)
        return counter
    return _recur(n, t, 0, memo)

ss([1,1,1,1,1], 3, {})
```

## 2.4. Kth Smallest Element in a BST
standard pre-order DFS
```
def ss(root):
    ss = [root]
    while ss:
        val = ss.pop()
        print(val.val)
        if val.right:
            ss.append(val.right)
        if val.left:
            ss.append(val.left)
```
iterative in-order travesal from root
```
def ss(root, k):
    n = 0
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

ss([5,3,6,2,4,null,null,1], 3)
```
dfs
```
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.n = k
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.n -= 1
            if self.n == 0:
                self.res = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return self.res
```

## 2.5. Course Schedule
- https://www.youtube.com/watch?v=EgI5nU9etnU&feature=youtu.be
- How to make adj list
```
li = [[1,0],[0,2],[1,3],[1,4],[3,4]]
premap = {}
```
```
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            premap[crs].append(preq)
        print(premap)
        visited = set()
        def dfs(crs):
            if not premap[crs]:
                print('has no dep')
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for cr in premap[crs]:
                if not dfs(cr): return False
            visited.remove(crs)
            premap[crs] = []
            return True
        
        for i in premap:
            if not dfs(i): return False
        return True
```
## 2.6. Course Schedule II
```
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        
        visited = set()
        inProgress = set()
        result = []
        
        def topologicalSort(course):
            nonlocal visited, inProgress, graph, result
            inProgress.add(course)
            if course in graph:
                for prereq in graph[course]:
                    if prereq in inProgress:
                        return False
                    if prereq not in visited:
                        status = topologicalSort(prereq)
                        if not status:
                            return False
            
            inProgress.remove(course)
            visited.add(course)
            result.append(course)
            return True
            
        
        for i in range(numCourses):
            if i in visited:
                continue
            if not topologicalSort(i):
                return []
        
        return result
```
cleaner way:
```
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        premap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            premap[crs].append(preq)
            
        visited, cycle =set(), set()
        
        def dfs(crs):
            # if cycle, stop immediately
            if crs in cycle:
                return False
            # if visited go on
            if crs in visited:
                return True
            # add current to check cycle
            cycle.add(crs)
            for cr in premap[crs]:
                if not dfs(cr):
                    return False
            # no cycle, thus add it to the queue
            order.append(crs)
            # remove cycle for the next iteration
            cycle.remove(crs)
            # this node is now saved
            visited.add(crs)
            return True
        
        for i in premap:
            if not dfs(i):
                return []
        return order
```
## 2.7. All nodes distance K in Binary Tree
make adjacency list from bst using queue:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build a adjacency list from bst
        premap = collections.defaultdict(list)
        def makeList(node):
            qq = [node]
            # use a queue to do BFS
            while qq:
                val = qq.pop(0)
                if val.left:
                    # unidirection graph, add child -> parent and p -> c
                    premap[val].append(val.left)
                    premap[val.left].append(val)
                    qq.append(val.left)
                if val.right:
                    premap[val].append(val.right)
                    premap[val.right].append(val)
                    qq.append(val.right)
            
        makeList(root)
        [print(k.val, [i.val for i in v]) for k,v in premap.items()]
```
```
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Create a hash table to store each node's parent using DFS.
        # Doing this will convert the problem to more of a graph problem.
        hashtable = {}  
        res = []
        def dfs(node, parent):
            if not node:
                return
            hashtable[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)   
            
        dfs(root, None)    
        
        # Once we have an adacency list (hash table), run a simple bfs search like any other graph problem
        q = deque([(target, 0)])
        visit = set()
        visit.add(target)
        while q:
            # Check if the leftmost value in queue has level == k. If so, return all values in q.
            # We will only have one level of nodes in the queue at a time.
            if q[0][1] == k:
                for node, level in q:
                    res.append(node.val)
                return res
            # BFS
            node, level = q.popleft()
            for nei in [node.left, node.right, hashtable[node]]:
                if nei and nei not in visit:
                    q.append((nei, level + 1))
                    visit.add(nei)
                    
        return res
        
# Time complexity = O(n)
# Space complexity = O(n)
```
another try
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build a adjacency list from bst
        premap = collections.defaultdict(list)
        res = []
        def makeList(node):
            qq = [node]
            # use a queue to do BFS
            while qq:
                val = qq.pop(0)
                if val.left:
                    # unidirection graph, add child -> parent and p -> c
                    premap[val].append(val.left)
                    premap[val.left].append(val)
                    qq.append(val.left)
                if val.right:
                    premap[val].append(val.right)
                    premap[val.right].append(val)
                    qq.append(val.right)
            
        makeList(root)
        #[print(k.val, [i.val for i in v]) for k,v in premap.items()]
        visited = set()
        visited.add(target.val)
        # use another queue to do BFS in the adjacency list
        qq = [(target, 0)]
        while qq:
            val, distance = qq.pop(0)
            if distance == k:
                res.append(val.val)
            for edge in premap[val]:
                if edge.val not in visited:
                    visited.add(edge.val)
                    qq.append((edge, distance + 1))
        return res
                
```
## 2.8. Path Sum II
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # final result list
        res = []
        def dfs(node,t,res,ss):
            if not node:
                return
            # edge check
            if not node.left and not node.right:
                if t == node.val:
                    ss = ss + [node.val]
                    res.append(ss)
            # advancing by replacing itself with 1 addition     
            ss = ss + [node.val]
            dfs(node.left,t - node.val,res,ss)
            dfs(node.right,t - node.val,res,ss)
            # at this point this will backtrack
        dfs(root,targetSum,res,[])
        print(res)
        return res
        
```
## 2.9. Path Sum III
```
Idea: Maintain prefix sums while doing dfs from root to leaf. If currentSum-prefixSum=targetSum, then we've found a path that has a value of target. If we encountered prefixSum n times, then we've found n such paths.

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

	# prefix sums encountered in current path
	sums = defaultdict(int)
	sums[0] = 1

	def dfs(root, total):
		count = 0
		if root:
			total += root.val
			# Can remove sums[currSum-targetSum] prefixSums to get target
			count = sums[total-targetSum]

			# Add value of this prefixSum
			sums[total] += 1
			# Explore children
			count += dfs(root.left, total) + dfs(root.right, total)
			# Remove value of this prefixSum (path's been explored)
			sums[total] -= 1

		return count

	return dfs(root, 0)
```
```
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res_count = 0

        def dfs(node):
            nonlocal res_count
            
            if not node:
                return []
            
            curr_paths = [0]

            if node.left:
                curr_paths += dfs(node.left)
            if node.right:
                curr_paths += dfs(node.right)
                
            for i in range(len(curr_paths)):
                curr_paths[i] += node.val
                if curr_paths[i] == targetSum:
                    res_count += 1
            
            return curr_paths

        dfs(root)
        return res_count
```
## 2.10. Maximum Product Subarray
- need to track min so when multiply by a negative that will give us the biggest positive
brute force
```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        for i in range(len(nums)):
            j = i + 1
            summ = nums[i]
            while j < len(nums):
                summ = summ * nums[j]
                j += 1
                print(summ)
                max_prod = max(max_prod, summ)
            print(summ, i, j, max_prod)
        return max_prod
```
```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = premax = premin = nums[0]
        for n in nums[1:]:
            currmin = min(premax * n, n, premin * n)
            currmax = max(premax * n, n, premin * n)
            premax = currmax
            premin = currmin
            final = max(premax, final)
        return final
```
## 2.11. Longest Increasing Subsequence
## 2.12. Longest Common Subsequence
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def recur(c1, c2):
            if c1 == len(text1) or c2 == len(text2):
                return 0
            if text1[c1] == text2[c2]:
                return 1 + recur(c1 + 1, c2 + 1)
            else:
                return max(recur(c1 + 1, c2), recur(c1, c2 + 1))
        return recur(0, 0)
```
- have to make 2-d grid for memo
- [[0 for j in range(len(text2))] for i in range(len(text1))]
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #@lru_cache(None)
        memo = [[0 for j in range(len(text2))] for i in range(len(text1))]
        def recur(c1, c2, memo):
            if c1 == len(text1) or c2 == len(text2):
                return 0
            if memo[c1][c2] == 0:
                if text1[c1] == text2[c2]:
                    memo[c1][c2] = 1 + recur(c1 + 1, c2 + 1, memo)
                else:
                    memo[c1][c2] = max(recur(c1 + 1, c2, memo), recur(c1, c2 + 1, memo))
            return memo[c1][c2]
        return recur(0, 0, memo)
```
## 2.13. House Robber
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            print(n, rob1, rob2, tmp)
            rob1 = rob2
            rob2 = tmp
        return rob2
```
tabulation
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        # make table same length as array with default
        dp = [0] * (len(nums))
        # set simple cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # start building max between choose the last one or (take current one and skip previous one)
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
        
```
## 2.14. Word Search
- this is backtracking problem, not optimization problem like dynamic programming

## 2.15. 0/1 Knapsack
tabulation
-
```
# for each item i
#   create new set which include i if total weight < cap
#       recursively process remaining
#   create a new set without item i, and recursively process
# return the set from above with higher profit
# recursive function with starting indexx and capacity changes depending on if uptaking the item or not
```
```
def solve_knapsack(profits, weights, capacity):
    dp = [[0 for j in range(capacity + 1)] for i in range(len(profits))]
    
    for i in range(1, capacity + 1):
        dp[0][i] = weights[0]
    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            p1, p2 = 0, 0
            if weights[i] <= j:
                p1 = profits[i] + dp[i - 1][j - weights[i]]
            p2 = dp[i - 1][j]
            dp[i][j] = max(p1, p2)
    print(dp)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()

```

## 2.16. Valid parentheses
```
class Solution:
    def isValid(self, s: str) -> bool:
        kl = ['{','[','(']
        kr = ['}',']',')']
        d1 = {}
        for i in range(len(kl)):
            d1[kr[i]] = kl[i]
        #print(d1)
        ss = []
        for i in s:
            if i in d1:
                #print(ss, d1[i])
                if not ss or ss[-1] != d1[i]:
                    return False
                else:
                    ss.pop()
            else:
                ss.append(i)
        return True if not ss else False
            
```
## 2.17. LRU cache
```
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]
```
