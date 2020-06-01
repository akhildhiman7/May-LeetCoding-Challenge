'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dik = {}
        for i in nums:
            dik[i] = dik.get(i, 0) + 1
        a, b = 0, 0
        for i, j in dik.items():
            if j > b:
                b = j
                a = i
        return a
