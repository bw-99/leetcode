class Solution:
    def farthest_index(self, tgt_idx):
        for i in range(tgt_idx):
            if i + self.nums[i] >= tgt_idx:
                return i
        
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        answer = 0
        self.nums = nums
        tgt_idx = len(nums)-1
        while (cur_idx:=self.farthest_index(tgt_idx)) is not None:
            answer+=1
            tgt_idx = cur_idx

            if cur_idx == 0:
                return answer
