"""
Given a string s, find the length of the longest substring without repeating 
characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
def subs(s):
    dic = {}
    for k, v in enumerate(s):
        if v not in dic:
            dic[v] = k
        else:
            print(dic.popitem()[1]+1)
            break























class Solution():
    def __init__(self, s):
        self.tbl = {}
        self.lt = s

    def length_substring(self):
        for i,v in enumerate(self.lt):
            for j, jv in enumerate(self.lt[i+1:]):
                if v == jv:
                    #print(i)
                    #print(j+i+1)
                    fst = i
                    snd = j+i+1
                    lent = snd - fst
                    self.tbl[fst] = lent
                    break
    def __repr__(self) -> str:
        return f"{self.tbl}"

l1 = "abcabcbb"
ret = Solution(l1)
ret.length_substring()
print(ret)
