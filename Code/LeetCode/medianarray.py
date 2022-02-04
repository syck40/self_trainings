"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""
l1 = [1,3,4]
l2 = [2,6,7, 10]

def median(l1, l2):
    ls1 = len(l1)
    ls2 = len(l2)
    n1 = n2 = 0
    l3 = []
    while n1 < ls1 and n2 < ls2:
        if l1[n1] < l2[n2]:
            l3.append(l1[n1])
            l3.append(l2[n2])
        else:
            l3.append(l2[n2])
            l3.append(l1[n1])
        n1 += 1
        n2 += 1
    print(l3)

median(l1,l2)
