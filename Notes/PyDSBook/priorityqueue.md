collection of prioritized elements allows arbitrary element insertion, and allows removal of element that has first priority.
when first added to queue, user designates priority through associated key, minimum key will be next to be removed from queue
using unsorted list vs sorted to implement PQ
unsorted: insertion at o(1) but finding/removing requires o(n)
sorted: find/remove at o(1) but insert at o(n) 
binaryheap: allows insertions/removals in log, heap achieves this through binary tree
heap: non decreasing from root to leaf
want heap to have smallest height as possible, tree must be complete -> 
heap insertion prompt up-heap bubbling
