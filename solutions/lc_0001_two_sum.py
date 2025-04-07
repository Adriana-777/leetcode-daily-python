
# LeetCode 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Tags: Array, Hash Table

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
