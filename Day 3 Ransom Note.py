'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

You may assume that both strings contain only lowercase letters.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dik1 = {}
        dik2 = {}
        for i in magazine:
            dik1[i] = dik1.get(i, 0) + 1
        for i in ransomNote:
            dik2[i] = dik2.get(i, 0) + 1
        for i in set(ransomNote):
            if i not in dik1 or dik2[i] > dik1[i]:
                return False
        return True
