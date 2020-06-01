'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dk = {}
        for i in range(len(s)):
            if s[i] in dk:
                dk[s[i]][0] = dk[s[i]][0]+1
                dk[s[i]][1] = i
            else:
                dk[s[i]] = [1, i]
        val = list(dk.values())
        val.sort(key = lambda x: x[0])
        for i, j in dk.items():
            print(i, j)
        print(val)
        if len(val) == 0:
            return -1
        if val[0][0] == 1:
            return val[0][1]
        else:
            return -1
