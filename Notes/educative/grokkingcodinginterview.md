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
      - [1.2.0.1. Intro](#1201-intro)
        - [1.2.0.1.1. Problems](#12011-problems)
          - [1.2.0.1.1.1. Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.](#120111-given-an-array-of-sorted-numbers-and-a-target-sum-find-a-pair-in-the-array-whose-sum-is-equal-to-the-given-target)
  - [Fast & Slow pinter](#fast--slow-pinter)
    - [Intro](#intro)
    - [Problems](#problems)
      - [Given the head of singly linkedlist, determine if it has a cycle in it or not](#given-the-head-of-singly-linkedlist-determine-if-it-has-a-cycle-in-it-or-not)
  - [1.3. Merge Intervals](#13-merge-intervals)
      - [1.3.0.1. Intro](#1301-intro)
      - [1.3.0.2. Problems](#1302-problems)
        - [1.3.0.2.1. Given list of intervals merge all overlapping intervals](#13021-given-list-of-intervals-merge-all-overlapping-intervals)


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
#### 1.2.0.1. Intro
sorted arrays or linkedlists vs non-sorted(sliding window)
##### 1.2.0.1.1. Problems
###### 1.2.0.1.1.1. Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
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

## Fast & Slow pinter
### Intro
- Useful for cyclic linkedlist or array
- Fast pointer should catch slow
### Problems
#### Given the head of singly linkedlist, determine if it has a cycle in it or not
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


## 1.3. Merge Intervals
#### 1.3.0.1. Intro
#### 1.3.0.2. Problems
##### 1.3.0.2.1. Given list of intervals merge all overlapping intervals
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
