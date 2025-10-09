class Solution:
    def reachableIndices(self, tgt_idx):
        for i in range(tgt_idx):
            if self.nums[i] + i >= tgt_idx:
                return i
        return None


    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        self.nums = nums
        tgt_idx = len(nums)-1

        is_first = False

        while (cur_idx := self.reachableIndices(tgt_idx)) is not None:
            if cur_idx == 0:
                is_first = True
                break
            tgt_idx = cur_idx
        
        return is_first