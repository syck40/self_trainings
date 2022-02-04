"""
Given an array of integers nums and an integer target, return indices of
 the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
 not use the same element twice.

You can return the answer in any order.


Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
tc = [12,2,11,7,7]
target = 9
def twosum(tc, target):
    tb = {}
    for k, v in enumerate(tc):
        try:
            tb[v].append(k)
        except KeyError:
            tb[v] = [k]
    print(tb)
twosum(tc,target)
