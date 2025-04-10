
### 🧠 通用模板代码 `nsum

from typing import List

class Solution:
    def nSum(self, nums: List[int], n: int, target: int) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, n, 0, target)

    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        res = []
        length = len(nums)

        # 至少 n 个数，并且最小值*n <= target <= 最大值*n 才有可能有解
        if n < 2 or length < n:
            return res

        # base case: 2Sum
        if n == 2:
            left, right = start, length - 1
            while left < right:
                sum_val = nums[left] + nums[right]
                if sum_val < target:
                    left += 1
                elif sum_val > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    # 跳过重复值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        else:
            # n >= 3
            for i in range(start, length):
                # 跳过重复数字
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # 递归缩小问题
                sub_res = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for subset in sub_res:
                    res.append([nums[i]] + subset)

        return res
