'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def helper(nums):
            start = 0
            end = len(nums) - 1
            ln = end
            while start <= end:
                mid = end - (end-start)//2
                if mid == 0 or mid == end: return nums[mid]
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: return nums[mid]
                if nums[mid] == nums[mid-1]:
                    if (mid - start + 1)%2 == 0:
                        start = mid+1
                    else:
                        end = mid - 2
                else:
                    if (mid - start + 2)%2 == 0:
                        start = mid+2
                    else:
                        end = mid - 1
            return nums[start]
        return helper(nums)
