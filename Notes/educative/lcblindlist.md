- [1. Blind list sorted by importance](#1-blind-list-sorted-by-importance)
  - [1. Clone Graph](#1-clone-graph)
  - [2. Coin Change](#2-coin-change)
  - [3. Target Sum](#3-target-sum)
  - [4. Kth Smallest Element in a BST](#4-kth-smallest-element-in-a-bst)
  - [5. Course Schedule](#5-course-schedule)
  - [6. Course Schedule II](#6-course-schedule-ii)
  - [7. All nodes distance K in Binary Tree](#7-all-nodes-distance-k-in-binary-tree)
- [2. Solutions](#2-solutions)
  - [1. Clone Graph](#1-clone-graph-1)
  - [2. Coin Change](#2-coin-change-1)
  - [3. Target Sum](#3-target-sum-1)
  - [4. Kth Smallest Element in a BST](#4-kth-smallest-element-in-a-bst-1)
  - [5. Course Schedule](#5-course-schedule-1)
  - [6. Course Schedule II](#6-course-schedule-ii-1)
  - [7. All nodes distance K in Binary Tree](#7-all-nodes-distance-k-in-binary-tree-1)

# 1. Blind list sorted by importance
## 1. Clone Graph
   - Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]] 
Output: [[2,4],[1,3],[2,4],[1,3]]
```
   - https://leetcode.com/problems/clone-graph/

## 2. Coin Change
   - You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.
   - https://leetcode.com/problems/clone-graph/
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```
## 3. Target Sum
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
## 4. Kth Smallest Element in a BST
  - Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
  - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
  - https://www.youtube.com/watch?v=5LUXSvjmGCw&feature=youtu.be
  - BST think sorted
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## 5. Course Schedule
- There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
- https://leetcode.com/problems/course-schedule/
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
## 6. Course Schedule II
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

## 7. All nodes distance K in Binary Tree
- Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```
 
- 
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
## 1. Clone Graph
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
## 2. Coin Change
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
## 3. Target Sum
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

## 4. Kth Smallest Element in a BST
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

## 5. Course Schedule
- https://www.youtube.com/watch?v=EgI5nU9etnU&feature=youtu.be
```
class Solution(object):
    def canFinish1(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = [i for i in range(numCourses) if not indegree[i]], set()
        while starts:
            node = starts.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
        return len(visited) == numCourses
        
    def canFinish2(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = deque([i for i in range(numCourses) if not indegree[i]]), set()
        while starts:
            node = starts.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
        return len(visited) == numCourses
    
    def canFinish(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        starts, visited = deque([i for i in range(numCourses) if not indegree[i]]), set()
        for start in starts:
            self.dfs(indegree, adj_list, start, visited)
        return len(visited) == numCourses
    
    def dfs(self, indegree, adj_list, start, visited):
        if start in visited:
            return
        visited.add(start)
        for neigh in adj_list[start]:
            indegree[neigh] -= 1
            if not indegree[neigh]:
                self.dfs(indegree, adj_list, neigh, visited)
```
## 6. Course Schedule II
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
## 7. All nodes distance K in Binary Tree
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
