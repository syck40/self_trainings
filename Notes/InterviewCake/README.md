# Big O
```
def printall(items):
    for i in items:
        for j in items[i+1:]:
            do_things()
    
    for i in items:
        do_things()
```
n^2, quadratic
2n^2, drop constant

```
def printall(items):
    print(items[0])
    x = len(items) / 2
    item = 0
    while item < x:
        do_things(items[item])
        item += 1
    for i in range(100):
        do_things()
```
O(1) + On/2 + o(100) = drop all constant = O(n)
Space complexity:
```
def list(n):
    inner_l = []
    for i in range(n):
        inner_l.append("hi")
    return inner_l
```
O(n) space for additional space not counting input

# Data Structures
CPU cache gets address 950 from RAM and its nearby 951, 952, sequential is faster than none.

decimal = base 10
binary = base 2

101 = 1x10^0 + 0x10^1, 1x10^2 = 1, 10, 100
101 = 1x2^0 + 0x2^1 + 1x2^2 = 1, 2, 4, 8, 16, 32, 64, 128 = 255 x 4 = 32 bit(4 billion) or 255 x 8 = 64 bit (10 billion billion 10^19)
01001110
256 128 64 32 16 8 4 2 1 = 64 + 14 = 78

Pointer eliminate wasted space but not as cache friendly, since it's no longer sequential

Dynamic array resize itself when running out of space.
Doubling during resizing is O(n) due to copying however this is offset due to O(1) appends rate, each append has an average cost or amortized cost of O(1).
Amortized = paying off debt gradually

Dynamic array so we don't need to specify size ahead of time but disadvantage is that some appends can be expensive

Linked list O(1) for append and prepend, dynamic array might have O(n) if run out of room

Prepend for dynamic array = O(n) since shuffling

Linked list is fast for append/prepend due to the nodes can be anywhere in memory but Array still has O(1) for lookup whereas lookup for linked list is O(n)

Hash table, hashing letters into number mod 30

The word "lies" in quotes. Arrows point from each character down to their corresponding number values, which are separated by plus signs and shown in sum to equal 429.
The result is 429. But what if we only have 30 slots in our array? We'll use a common trick for forcing a number into a specific range: the modulus operator (%)

Modding our sum by 30 ensures we get a whole number that's less than 30 (and at least 0):

Summary:
Array is fast due to caching nearby memory, array is fix block and same size.  Downside is size must be known.

Array of pointer could help minimize wasted space but tradeoff is less efficient caching.

Dynamic array grows by doubling in size and moving all items, trade

Hash table is arrays with artitrary keys provided by hashing function
# Logarithms
logxY, what power must we raise base x to to get Y

n * (1/2)^x = 1
(1/2)^x = 1/n
n = 2^x
log2^n = log2^x
log(1/2) = log 1/n

Sorting cost O(nlog2^n) -> best worst-case

merge sort, divide and merge

```
def merge_sort(list):
    if len(list) < 2:
        return list
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    sorted_li = []
    current_left = 0
    current_right = 0
    while len(sorted_li) < len(left) + len(right):
        
```
# Array

# Array Slicing

# In-Place Algorithms

# Dynamic Array

# Hashing

# Hash Table

# Greedy Algo

# Binary Search

# Binary Tree

# Graph

# BFS

# DFS

# Overlapping Subproblems

# Memoization

# Bottom-Up Algo

# Queues and Stacks

# Linked list

