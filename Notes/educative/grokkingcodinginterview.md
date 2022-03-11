# 1. Interview patterns
- [1. Interview patterns](#1-interview-patterns)
  - [1.1. Sliding Window](#11-sliding-window)
    - [1.1.1. Intro](#111-intro)
    - [1.1.2. Psudocode](#112-psudocode)
    - [1.1.3. Bruteforce](#113-bruteforce)
    - [1.1.4. Better approach](#114-better-approach)
    - [1.1.5. Problems](#115-problems)
      - [1.1.5.1. Max Sum Subarray of Size K](#1151-max-sum-subarray-of-size-k)
      - [1.1.5.2. Smallest Subarray With a Greater Sum](#1152-smallest-subarray-with-a-greater-sum)
      - [1.1.5.3. Longest substring with no more than K distinct char](#1153-longest-substring-with-no-more-than-k-distinct-char)
  - [1.2. Two Pointers](#12-two-pointers)
    - [1.2.1. Intro](#121-intro)
    - [1.2.2. Problems](#122-problems)
      - [1.2.2.1. Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.](#1221-given-an-array-of-sorted-numbers-and-a-target-sum-find-a-pair-in-the-array-whose-sum-is-equal-to-the-given-target)
  - [1.3. Fast & Slow Pointers](#13-fast--slow-pointers)
    - [1.3.1. Intro](#131-intro)
    - [1.3.2. Problems](#132-problems)
      - [1.3.2.1. Given the head of singly linkedlist, determine if it has a cycle in it or not](#1321-given-the-head-of-singly-linkedlist-determine-if-it-has-a-cycle-in-it-or-not)
      - [1.3.2.2. Given the head of a LinkedList with a cycle, find the length of the cycle.](#1322-given-the-head-of-a-linkedlist-with-a-cycle-find-the-length-of-the-cycle)
      - [1.3.2.3. Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.](#1323-given-the-head-of-a-singly-linkedlist-that-contains-a-cycle-write-a-function-to-find-the-starting-node-of-the-cycle)
  - [1.4. Merge Intervals](#14-merge-intervals)
    - [1.4.1. Intro](#141-intro)
    - [1.4.2. Problems](#142-problems)
      - [1.4.2.1. Given list of intervals merge all overlapping intervals](#1421-given-list-of-intervals-merge-all-overlapping-intervals)
  - [1.5. Cyclic Sort](#15-cyclic-sort)
    - [1.5.1. Intro](#151-intro)
    - [1.5.2. Problems](#152-problems)
      - [1.5.2.1. c_sort](#1521-c_sort)
  - [1.6. Reversal of LinkedList](#16-reversal-of-linkedlist)
    - [1.6.1. Intro](#161-intro)
    - [1.6.2. Problems](#162-problems)
      - [1.6.2.1. In place reversal](#1621-in-place-reversal)
      - [1.6.2.2. Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.](#1622-given-the-head-of-a-linkedlist-and-two-positions-p-and-q-reverse-the-linkedlist-from-position-p-to-q)
  - [1.7. Tree Breadth First Search](#17-tree-breadth-first-search)
    - [1.7.1. Intro](#171-intro)
    - [1.7.2. Problems](#172-problems)
      - [1.7.2.1. BFS](#1721-bfs)
      - [1.7.2.2. Zigzag BFS](#1722-zigzag-bfs)
  - [1.8. DFS](#18-dfs)
    - [1.8.1. Intro](#181-intro)
    - [1.8.2. Problems](#182-problems)
      - [1.8.2.1. Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.](#1821-given-a-binary-tree-and-a-number-s-find-if-the-tree-has-a-path-from-root-to-leaf-such-that-the-sum-of-all-the-node-values-of-that-path-equals-s)
      - [1.8.2.2. Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.](#1822-given-a-binary-tree-and-a-number-s-find-all-paths-from-root-to-leaf-such-that-the-sum-of-all-the-node-values-of-each-path-equals-s)
  - [1.9. Two Heaps](#19-two-heaps)
    - [1.9.1. Intro](#191-intro)
    - [1.9.2. Psudo](#192-psudo)
    - [1.9.3. Problems](#193-problems)
      - [1.9.3.1. Design a class to calculate the median of a number stream.](#1931-design-a-class-to-calculate-the-median-of-a-number-stream)
  - [1.10. Subsets](#110-subsets)
    - [1.10.1. Intro](#1101-intro)
    - [1.10.2. Problems](#1102-problems)
      - [1.10.2.1. Given a set with distinct elements, find all of its distinct subsets.](#11021-given-a-set-with-distinct-elements-find-all-of-its-distinct-subsets)
      - [1.10.2.2. Given a set of numbers that might contain duplicates, find all of its distinct subsets.](#11022-given-a-set-of-numbers-that-might-contain-duplicates-find-all-of-its-distinct-subsets)
      - [1.10.2.3. Permutations](#11023-permutations)
  - [1.11. Binary Search](#111-binary-search)
    - [1.11.1. Intro](#1111-intro)
    - [1.11.2. Problems](#1112-problems)
      - [1.11.2.1. Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.](#11121-given-a-sorted-array-of-numbers-find-if-a-given-number-key-is-present-in-the-array-though-we-know-that-the-array-is-sorted-we-dont-know-if-its-sorted-in-ascending-or-descending-order-you-should-assume-that-the-array-can-have-duplicates)
      - [1.11.2.2. Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.](#11122-given-an-array-of-numbers-sorted-in-an-ascending-order-find-the-ceiling-of-a-given-number-key-the-ceiling-of-the-key-will-be-the-smallest-element-in-the-given-array-greater-than-or-equal-to-the-key)
  - [1.12. Bit wise XOR](#112-bit-wise-xor)
    - [1.12.1. Intro](#1121-intro)
    - [1.12.2. Problems](#1122-problems)
      - [1.12.2.1. Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.](#11221-given-an-array-of-n1-integers-in-the-range-from-1-to-n-find-the-one-number-that-is-missing-from-the-array)
      - [1.12.2.2. In a non-empty array of integers, every number appears twice except for one, find that single number.](#11222-in-a-non-empty-array-of-integers-every-number-appears-twice-except-for-one-find-that-single-number)
  - [1.13. Top/Smallest/frequent K elements](#113-topsmallestfrequent-k-elements)
    - [1.13.1. Intro](#1131-intro)
    - [1.13.2. Problems](#1132-problems)
      - [1.13.2.1. Given an unsorted array of numbers, find the ‘K’ largest numbers in it.](#11321-given-an-unsorted-array-of-numbers-find-the-k-largest-numbers-in-it)
      - [1.13.2.2. Given an unsorted array of numbers, find Kth smallest number in it.](#11322-given-an-unsorted-array-of-numbers-find-kth-smallest-number-in-it)
  - [1.14. K-way Merge](#114-k-way-merge)
    - [1.14.1. Intro](#1141-intro)
    - [1.14.2. Problems](#1142-problems)
      - [1.14.2.1. Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.](#11421-given-an-array-of-k-sorted-linkedlists-merge-them-into-one-sorted-list)
      - [1.14.2.2. Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.](#11422-given-m-sorted-arrays-find-the-kth-smallest-number-among-all-the-arrays)
  - [1.15. Dynamic Programming - 0/1 Knapsack](#115-dynamic-programming---01-knapsack)
    - [1.15.1. Intro](#1151-intro)
    - [1.15.2. Problems](#1152-problems)
      - [1.15.2.1. N items, C capacity, max profit, each item can only be selected once](#11521-n-items-c-capacity-max-profit-each-item-can-only-be-selected-once)
      - [LC: Coin Change](#lc-coin-change)
  - [1.16. Topological Sort(directed graph)](#116-topological-sortdirected-graph)
    - [1.16.1. Intro](#1161-intro)
    - [1.16.2. Problems](#1162-problems)
      - [1.16.2.1. Find if a given Directed Graph has a cycle or not](#11621-find-if-a-given-directed-graph-has-a-cycle-or-not)
  - [1.17. Misc](#117-misc)


## 1.1. Sliding Window
### 1.1.1. Intro
Given an array calculate something from subarrays within it.
- [1,3,2,6,-1,4,1,8,2], K=5
- Find avg of all subarrays of Kcontignous elements in given array
### 1.1.2. Psudocode
1. get avg of the first K number
2. get avg of next K number

### 1.1.3. Bruteforce
```
ret = []
def bf(n, k):
    for i in range(len(n)-k+1):
        sum = 0
        j = i
        while j - i < k:
            sum += n[j]
            j+=1
        avg = sum/k
        ret.append(avg)
    print(ret)
```
O(N*K)
### 1.1.4. Better approach
```
ret = []
def bf(n, k):
    sum, start = 0, 0
    for end in range(len(n)):
        sum += n[end]
        if end+1 >= k:
            ret.append(sum/k)
            sum -= n[start]
            start += 1
    print(ret)
```
### 1.1.5. Problems
#### 1.1.5.1. Max Sum Subarray of Size K
- Find max sum of continous subarray of size K
- [2, 1, 5, 1, 3, 2], k=3 
```
def bf(n, k):
    sum, start = 0, 0
    tmpMax = 0
    for end in range(len(n)):
        sum += n[end]
        if end >= k:
            sum -= n[start]
            tmpMax = max(tmpMax, sum)
            start+=1
    print(tmpMax)
bf([2, 1, 5, 1, 3, 2], 3)
```

#### 1.1.5.2. Smallest Subarray With a Greater Sum
- Find the length of the smallest continguous subarray whos sum is greater than or equal to K
- [2, 1, 5, 2, 3, 2], S=7
```
def bf(n,k):
    sum, start = 0, 0
    smallest = 100
    for end in range(len(n)):
        sum += n[end]
        if sum >= k:
            smallest = min(smallest, end-start+1)
            sum -= n[start]
            start += 1
    print(smallest)
bf([2, 1, 5, 2, 8], 7 )
```
- sliding windows size is NOT fixed!!
#### 1.1.5.3. Longest substring with no more than K distinct char
- String="araaci", K=2
```
def bf(n, k):
    mapp = {}
    start = 0
    length = 0
    maxlength = 0
    for c in range(len(n)):
        if n[c] in mapp:
            mapp[n[c]] += 1
            length += 1
            if mapp[n[c]] == k:
                print(length)
                maxlength = max(length, maxlength)
                length = 0
                start += 1
                mapp = {}
        else:
            mapp[n[c]] = 1
            length += 1
    print(maxlength)
bf("cbbebi", 2)
```
## 1.2. Two Pointers
### 1.2.1. Intro
sorted arrays or linkedlists vs non-sorted(sliding window)
### 1.2.2. Problems
#### 1.2.2.1. Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
- Since it's sorted, 1 pointer at start and 1 pointer at the end
- Compare sum from 2 pointers with target, if small increase 1st pointer else decrease 2nd pointer
```
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

def bf(n, t):
    low = 0
    high = len(n) - 1
    val = n[low] + n[high]
    while val != t and low < len(n) and high >= 0:
        if val > t:
            high -= 1
        else:
            low += 1
        val = n[low] + n[high]
    ret = [low, high]
    print(ret)
bf([1,2,3,4,6], 6)
```

## 1.3. Fast & Slow Pointers
### 1.3.1. Intro
- Useful for cyclic linkedlist or array
- Fast pointer should catch slow
### 1.3.2. Problems
#### 1.3.2.1. Given the head of singly linkedlist, determine if it has a cycle in it or not
- 
```
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

visited = set()

def has_cycle(head):
  # TODO: Write your code here
  if not head:
    return False
  if head.value in visited:
    return True
  else:
    visited.add(head.value)
  return has_cycle(head.next)

###
def has_cycle(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      return True  # found the cycle
  return False
###

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()
```
#### 1.3.2.2. Given the head of a LinkedList with a cycle, find the length of the cycle.
- We can use the above solution to find the cycle in the LinkedList. Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.
```
def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      return calculate_cycle_length(slow)

  return 0


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length
```

#### 1.3.2.3. Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
- find out the length of cycle, put 1 pointer at 0 + length, another pointer at 0, see when they meet
```

def find_cycle_start(head):
  cycle_length = 0
  # find the LinkedList cycle
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      cycle_length = calculate_cycle_length(slow)
      break
  return find_start(head, cycle_length)


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  # move pointer2 ahead 'cycle_length' nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1
```


## 1.4. Merge Intervals
### 1.4.1. Intro
### 1.4.2. Problems
#### 1.4.2.1. Given list of intervals merge all overlapping intervals
- [[1,4], [2,5], [7,9]], [[1,5], [7,9]]
- sort first
- start from n[0] and set pointer to n[0].start/end, create interval obj to append during for loop, move start/end pointer to newly created

```
class Interval():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def ss(n):
    n.sort(key=lambda x: x.x)
    ret = []
    start = n[0].x
    end = n[0].y
    for i in range(1, len(n)):
        inter = n[i]
        if inter.x <= end:
            end = max(inter.y, end)
        else:
            ret.append(Interval(start, end))
            start = inter.x
            end = inter.y
    ret.append(Interval(start,end))
    [print(i.x,i.y) for i in ret]
    return ret

ss([Interval(1,3), Interval(1,4),Interval(2,3),Interval(2,5),Interval(1,6)])
```
## 1.5. Cyclic Sort
### 1.5.1. Intro
- Unsorted, array of int, from 1 to n, can have duplicates.  Find all missing numbers
- https://emre.me/categories/#coding-patterns
- This approach is quite useful when dealing with numbers in a given range and asking to find the duplicates/missing ones etc.

When the problem involving arrays containing numbers in a given range, you should think about Cyclic Sort pattern.

### 1.5.2. Problems
#### 1.5.2.1. c_sort
- We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.
```
def bf(n):
    for i in range(len(n)):
        print(n)
        if n[n[i] - 1] != n[i] and n[n[i]-1] < len(n):
            n[i], n[n[i] - 1] = n[n[i] - 1], n[i]
    print(n)
bf([2, 6, 4, 3, 1, 5])
def bf(n):
    for i in range(len(n)):
        print(n)
        if n[n[i] - 1] != n[i] and n[n[i]-1] < len(n):
            n[i], n[n[i] - 1] = n[n[i] - 1], n[i]
    print(n)
bf([2, 6, 4, 3, 1, 5])
```

## 1.6. Reversal of LinkedList
### 1.6.1. Intro
### 1.6.2. Problems
#### 1.6.2.1. In place reversal
```
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  # TODO: Write your code here
  last = None
  prev = curr = head
  next = curr.next
  curr.next = None
  while next:
    curr = next
    next = curr.next
    curr.next = prev
    prev = curr
  last = prev
  return last

###
def reverse(head):
  previous, current, next = None, head, None
  while current is not None:
    next = current.next  # temporarily store the next node
    current.next = previous  # reverse the current node
    previous = current  # before we move to the next node, point previous to the current node
    current = next  # move on the next node
  return previous
###

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
```
#### 1.6.2.2. Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

## 1.7. Tree Breadth First Search
### 1.7.1. Intro
- Queue
### 1.7.2. Problems
#### 1.7.2.1. BFS
```
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result
  qq = [root]
  while qq:
    lvl = len(qq)
    sum = 0
    for _ in range(lvl):
      val = qq.pop(0)
      sum += val.val
      if val.left:
        qq.append(val.left)
      if val.right:
        qq.append(val.right)
    result.append(sum / lvl)

  return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level order traversal: " + str(traverse(root)))

```
#### 1.7.2.2. Zigzag BFS
- keep track of current level, queue size = current level if do a for loop for number of times == queue size

## 1.8. DFS
### 1.8.1. Intro
- O(H) where H is max height of the tree
### 1.8.2. Problems
#### 1.8.2.1. Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

```
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if not root:
    return False
  if not root.left and not root.right and root.val == sum:
    return True

  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(has_path(root, 23)))
print("Tree has path: " + str(has_path(root, 16)))
```
#### 1.8.2.2. Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
```
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  # TODO: Write your code here
  def _recur(root, currpath, tar):
    if not root:
      print(currpath)
      return
    currpath.append(root.val)
    print(tar)
    tar -= root.val
    if tar == 0:
      print(currpath)
    _recur(root.left, currpath, tar)
    _recur(root.right, currpath, tar)
    currpath.pop()
  _recur(root, [], sum)
  return allPaths

###
    def pathSum(root, targetSum):
        ret = []
        def _recur(root, targetSum, curr):
            if not root:
                return
            curr = curr + [root.val]
            #curr.append(root.val)
            print(curr)
            if not root.left and not root.right and root.val == targetSum:
                ret.append(curr)
                return
            _recur(root.left, targetSum - root.val, curr)
            _recur(root.right, targetSum - root.val, curr)
            
        _recur(root, targetSum, [])
        print(ret)

###
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
print("Tree paths with sum " + str(sum) +
      ": " + str(find_paths(root, sum)))
```

## 1.9. Two Heaps
### 1.9.1. Intro
- where we are given a set of elements such that we can divide them into two parts. We are interested in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an efficient approach to solve such problems.
### 1.9.2. Psudo
1. We can store the first half of numbers (i.e., smallNumList) in a Max Heap. We should use a Max Heap as we are interested in knowing the largest number in the first half.
2. We can store the second half of numbers (i.e., largeNumList) in a Min Heap, as we are interested in knowing the smallest number in the second half.
3. Inserting a number in a heap will take O(logN), which is better than the brute force approach.
### 1.9.3. Problems
#### 1.9.3.1. Design a class to calculate the median of a number stream.
-  The median is the middle value in an ordered integer list. So a brute force solution could be to maintain a sorted list of all numbers inserted in the class so that we can efficiently return the median whenever required.
- Can we utilize the fact that we don’t need the fully sorted list.  We are only interested in finding the middle element?
- one half to store all the smaller numbers (let’s call it smallNumList) and one half to store the larger numbers (let’s call it largNumList). The median of all the numbers will either be the largest number in the smallNumList or the smallest number in the largNumList. If the total number of elements is even, the median will be the average of these two numbers.
1. insertNum(3): We can insert a number in the Max Heap (i.e. first half) if the number is smaller than the top (largest) number of the heap. After every insertion, we will balance the number of elements in both heaps, so that they have an equal number of elements. If the count of numbers is odd, let’s decide to have more numbers in Max Heap than the Min Heap.
2. insertNum(1): As ‘1’ is smaller than ‘3’, let’s insert it into the Max Heap. Now, we have two elements in the Max Heap and no elements in Min Heap. Let’s take the largest element from the Max Heap and insert it into the Min Heap, to balance the number of elements in both heaps.
3. findMedian(): As we have an even number of elements, the median will be the average of the top element of both the heaps -> 
(1+3)/2=2.0
4. insertNum(5): As ‘5’ is greater than the top element of the Max Heap, we can insert it into the Min Heap. After the insertion, the total count of elements will be odd. As we had decided to have more numbers in the Max Heap than the Min Heap, we can take the top (smallest) number from the Min Heap and insert it into the Max Heap.
5. findMedian(): Since we have an odd number of elements, the median will be the top element of Max Heap -> 3. An odd number of elements also means that the Max Heap will have one extra element than the Min Heap.
6. insertNum(4): Insert ‘4’ into Min Heap.

```
from heapq import *


class MedianOfAStream:

  maxHeap = []  # containing first half of numbers
  minHeap = []  # containing second half of numbers

  def insert_num(self, num):
    if not self.maxHeap or -self.maxHeap[0] >= num:
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))

  def find_median(self):
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0


medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(5)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(4)
print("The median is: " + str(medianOfAStream.find_median()))
```
## 1.10. Subsets
### 1.10.1. Intro
- BFS
### 1.10.2. Problems
#### 1.10.2.1. Given a set with distinct elements, find all of its distinct subsets.
- Input: [1, 3]
Output: [], [1], [3], [1,3]
```
def find_subsets(nums):
  subsets = []
  # TODO: Write your code here
  subsets.append([])
  for i in nums:
    n = len(subsets)
    for j in range(n):
      if subsets[j]:
        ret = [subsets[j]]
        ret.append(i)
      else:
        ret = [i]
      subsets.append(ret)
  return subsets

find_subsets([1, 3, 3])
print("Here is the list of subsets: " + str(find_subsets([1, 3])))
print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
```
#### 1.10.2.2. Given a set of numbers that might contain duplicates, find all of its distinct subsets.
- sort it with list.sort(nums)
#### 1.10.2.3. Permutations
- Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
```
from collections import deque


def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result
find_permutations([1, 3, 5])
```
## 1.11. Binary Search
### 1.11.1. Intro
### 1.11.2. Problems
#### 1.11.2.1. Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.
- Input: [4, 6, 10], key = 10
Output: 2
```
def ss(n, k):
  low = 0
  high = len(n) - 1
  ascending = True
  if n[0] > n[1]:
    ascending = False
  while low <= high:
    mid = (low + high) // 2
    if n[mid] == k:
      return mid

    if ascending:
      if n[mid] < k:
        low = mid + 1
      else:
        high = mid - 1
    else:
      if n[mid] < k:
        high = mid - 1
      else:
        low = mid + 1
  return -1
ss([4,6,10], 10)
```
#### 1.11.2.2. Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
- Input: [4, 6, 10], key = 6
Output: 1
- Input: [1, 3, 8, 10, 15], key = 12
Output: 4
```
def ss(n, k):
  low, high = 0, len(n) - 1
  while low <= high:
    mid = (low + high) // 2
    if n[mid] == k:
      return mid
    elif n[mid] < k:
      low = mid + 1
    else:
      return mid
  return -1
ss([4, 6, 10], 6)
```
## 1.12. Bit wise XOR
### 1.12.1. Intro
- XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise. In other words, it only returns 1 if exactly one bit is set to 1 out of the two bits in comparison.
### 1.12.2. Problems
#### 1.12.2.1. Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.
- Input: 1, 5, 2, 6, 4
Answer: 3
- Remember the important property of XOR that it returns 0 if both the bits in comparison are the same. In other words, XOR of a number with itself will always result in 0. This means that if we XOR all the numbers in the input array with all numbers from the range 1 to n then each number in the input is going to get zeroed out except the missing number. 

```
def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2

arr = [1, 5, 2, 6, 4] 
print('Missing number is:' + str(find_missing_number(arr)))
```
```
Taking XOR of a number with itself returns 0, e.g.,

1 ^ 1 = 0
29 ^ 29 = 0
Taking XOR of a number with 0 returns the same number, e.g.,

1 ^ 0 = 1
31 ^ 0 = 31
XOR is Associative & Commutative, which means:

(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
```
#### 1.12.2.2. In a non-empty array of integers, every number appears twice except for one, find that single number.
- Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
- hashmap and traverse, If number is already present in HashMap, remove it.
If number is not present in HashMap, add it.
In the end, only number left in the HashMap is our required single number.
- Recall the following two properties of XOR:

It returns zero if we take XOR of two same numbers.
It returns the same number if we XOR with zero.
So we can XOR all the numbers in the input; duplicate numbers will zero out each other and we will be left with the single number.

## 1.13. Top/Smallest/frequent K elements
### 1.13.1. Intro
- Think heap
### 1.13.2. Problems
#### 1.13.2.1. Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
- Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
```
import heapq
def ss(n, k):
  ret = []
  for i in range(k):
    heapq.heappush(ret, n[i])
  for j in range(k, len(n)):
    if n[j] > ret[0]:
      heapq.heapreplace(ret, n[j])
  print(ret)
ss([3,1,5,12,2,11], 3)
```
- max heap
```
import heapq
def ss(n, k):
  ret = []
  kk = []
  for i in range(len(n)):
    heapq.heappush(ret, -n[i])
  for j in range(k):
    v = heapq.heappop(ret)
    kk.append(-v)
  print(kk)
ss([3,1,5,12,2,11], 3)
```
#### 1.13.2.2. Given an unsorted array of numbers, find Kth smallest number in it.
- Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
- Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].
```
from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]

print("Kth smallest number is: " +
      str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

# since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
print("Kth smallest number is: " +
      str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

print("Kth smallest number is: " +
      str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


```

## 1.14. K-way Merge
### 1.14.1. Intro
- Problems with a list of sorted arrays
- Whenever we are given ‘K’ sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. We can push the smallest (first) element of each sorted array in a Min Heap to get the overall minimum. While inserting elements to the Min Heap we keep track of which array the element came from. We can, then, remove the top element from the heap to get the smallest element and push the next element from the same array, to which this smallest element belonged, to the heap. We can repeat this process to make a sorted traversal of all elements.
### 1.14.2. Problems
#### 1.14.2.1. Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
- Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
- Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]

```
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None


def merge_lists(lists):
  minHeap = []

  # put the root of each list in the min heap
  for root in lists:
    if root is not None:
      heappush(minHeap, root)

  # take the smallest(top) element form the min-heap and add it to the result
  # if the top element has a next element add it to the heap
  resultHead, resultTail = None, None
  while minHeap:
    node = heappop(minHeap)
    if resultHead is None:
      resultHead = resultTail = node
    else:
      resultTail.next = node
      resultTail = resultTail.next

    if node.next is not None:
      heappush(minHeap, node.next)

  return resultHead


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

result = merge_lists([l1, l2, l3])
print("Here are the elements form the merged list: ", end='')
while result != None:
  print(str(result.value) + " ", end='')
  result = result.next
```
#### 1.14.2.2. Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
- Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
- We can start merging all the arrays, but instead of inserting numbers into a merged list, we will keep count to see how many elements have been inserted in the merged list. Once that count is equal to ‘K’, we have found our required number.

A big difference from Merge K Sorted Lists is that in this problem, the input is a list of arrays compared to LinkedLists. This means that when we want to push the next number in the heap we need to know what the index of the current number in the current array was. To handle this, we will need to keep track of the array and the element indices.
```
def find_Kth_smallest(lists, k):
  number = -1
  # TODO: Write your code here
  return number

print("Kth smallest number is: " +
      str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
```

## 1.15. Dynamic Programming - 0/1 Knapsack
### 1.15.1. Intro
- A technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.
- Overlapping subproblems
- If overall optimal solution can be constructed from optimal solutions of its subproblems.
- Top down with memoization or bottom-up with tabulation
### 1.15.2. Problems
#### 1.15.2.1. N items, C capacity, max profit, each item can only be selected once
- Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
```
def solve_knapsack(profits, weights, capacity):
  def _recur(profits, weights, capacity, curr):
    if capacity <= 0 or curr >= len(profits):
      return 0
    profit1 = 0
    if weights[curr] <= capacity:
      profit1 = profits[curr] + _recur(profits, weights, capacity - weights[curr], curr + 1)
    profit2 = _recur(profits, weights, capacity, curr + 1)

    return max(profit1, profit2)

  return _recur(profits, weights, capacity, 0)


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
```
#### LC: Coin Change
- https://leetcode.com/problems/coin-change/
- You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
- Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
- greedy, start from highest -> itself -> next highest, but doesn't yield fewest.
- DFS backtracking, brute force decision tree N number, N options
```
def ss(n, tar):
  def _recur(n, tar, memo):
    if tar == 0:
      return 0
    if tar < 0:
      return 0
    for i in n:
      print(1 + _recur(n, tar - i, memo))
  _recur(n, 7, {})
ss([1,2,5], 11)
```
7
1 3 4 5
6 4 3 2
5 3 2 1

## 1.16. Topological Sort(directed graph)
- Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
- The basic idea behind the topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from U to V then U≤V i.e., U comes before V in the ordering. Here are a few fundamental concepts related to topological sort:
- Source: Any node that has no incoming edge and has only outgoing edges is called a source.

Sink: Any node that has only incoming edges and no outgoing edge is called a sink.

So, we can say that a topological ordering starts with one of the sources and ends at one of the sinks.

A topological ordering is possible only when the graph has no directed cycles, i.e. if the graph is a Directed Acyclic Graph (DAG). If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.
- a. Initialization

We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices.
To find the sources, we will keep a HashMap to count the in-degrees i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.
b. Build the graph and find in-degrees of all vertices

We will build the graph from the input and populate the in-degrees HashMap.
c. Find all sources

All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.
d. Sort

For each source, do the following things:
Add it to the sorted list.
Get all of its children from the graph.
Decrement the in-degree of each child by 1.
If a child’s in-degree becomes ‘0’, add it to the sources Queue.
Repeat step 1, until the source Queue is empty.
```
from collections import deque


def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder

print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
```
### 1.16.1. Intro
- Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
### 1.16.2. Problems
#### 1.16.2.1. Find if a given Directed Graph has a cycle or not
- if can't determine the topological ordering then it has a cycle

## 1.17. Misc
- list.append vs list + [new] vs list.extend()
- The concatenation operator + is a binary infix operator which, when applied to lists, returns a new list containing all the elements of each of its two operands. The list.append() method is a mutator on list which appends its single object argument (in your specific example the list c) to the subject list. In your example this results in c appending a reference to itself (hence the infinite recursion).
- heapsort with import heapq
```
import heapq
def heapsort(iterable):
  h = []
  for value in iterable:
      heapq.heappush(h, value)
  return [heapq.heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

