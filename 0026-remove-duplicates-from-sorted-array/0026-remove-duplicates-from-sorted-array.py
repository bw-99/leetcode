class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        for end in range(1, len(nums)):
            if nums[end] != nums[start]:
                start += 1
                nums[start] = nums[end]
        return start + 1