- [Problems](#problems)
  - [Arrays](#arrays)
    - [Rotate array by N](#rotate-array-by-n)
  - [Linked List](#linked-list)
    - [Reversal](#reversal)
  - [Permutation](#permutation)
    - [kth permutation](#kth-permutation)
  - [Strings](#strings)
    - [Reverse words in a sentence](#reverse-words-in-a-sentence)
- [Solutions](#solutions)
  - [Arrays](#arrays-1)
    - [Rotate array by N](#rotate-array-by-n-1)
  - [Linked List](#linked-list-1)
    - [Reversal](#reversal-1)
  - [Permutation](#permutation-1)
    - [kth permutation](#kth-permutation-1)
  - [Strings](#strings-1)
    - [Reverse words in a sentence](#reverse-words-in-a-sentence-1)
  - [Trees](#trees)
    - [Check if 2 bst are identical](#check-if-2-bst-are-identical)
# Problems
## Arrays
### Rotate array by N
- 
```
We’re given an array of integers, nums. Rotate the array by n elements, where n is an integer:

For positive values of n, perform a right rotation.
For negative values of n, perform a left rotation.
Make sure we make changes to the original array.
```
```
nums = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
n = 2
```
## Linked List
### Reversal
- inplace reversal of a linked list
## Permutation
### kth permutation
- Given 2 numbers n and k find kth permutation of n
## Strings
### Reverse words in a sentence
# Solutions
## Arrays
### Rotate array by N
- negative rotation move to left, positive move to right
- key is reversing array for the whole arr first, then reverse the 0 - n part then n - len(arr)
- reversing an array using 2 pointers and while start < end, swap with tmp value and increment/decrement pointers
## Linked List
### Reversal
- 2 pointers, 1st point to head, 2nd to head's next
## Permutation
### kth permutation
## Strings
### Reverse words in a sentence
## Trees
### Check if 2 bst are identical
- 
