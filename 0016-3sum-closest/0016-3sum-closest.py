from typing import List

class Solution:
    def _twopointer(self, nums, i, target, best):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(best - target):
                best = s

            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return s, True  # exact hit
        return best, False

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            best, hit = self._twopointer(nums, i, target, best)
            if hit:
                return best
        return best