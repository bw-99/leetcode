class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start = 0
        for end in range(1, len(nums)):
            if nums[start]==nums[end]:
                continue
            
            start+=1
            nums[start] = nums[end]
        return start+1