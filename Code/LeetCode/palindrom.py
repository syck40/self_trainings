"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad" dabab
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
def pal(s):
    l1 = [i for i in s]
    l2 = list(reversed(l1))
    ret = []
    print(l1, l2)
    for k, v in enumerate(l1):
        if l1[k] == l2[k]:
            ret = []
            ret.append(l1[k])
            k += 1
            while k < len(l1) and l1[k] == l2[k]:
                ret.append(l1[k])
                k += 1
            print(ret)
        

pal("cbabd")
