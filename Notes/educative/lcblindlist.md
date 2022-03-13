- [1. Blind list sorted by importance](#1-blind-list-sorted-by-importance)
  - [1. Clone Graph](#1-clone-graph)
  - [2. Coin Change](#2-coin-change)
  - [3. Target Sum](#3-target-sum)
  - [4. Kth Smallest Element in a BST](#4-kth-smallest-element-in-a-bst)
- [2. Solutions](#2-solutions)
  - [1. Clone Graph](#1-clone-graph-1)
  - [2. Coin Change](#2-coin-change-1)
  - [3. Target Sum](#3-target-sum-1)
  - [4. Kth Smallest Element in a BST](#4-kth-smallest-element-in-a-bst-1)

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
