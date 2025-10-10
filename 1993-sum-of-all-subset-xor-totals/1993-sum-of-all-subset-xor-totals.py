class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        answer = 0

        def dfs(pos, q):
            nonlocal answer
            if q:
                tmp_answer = q[0]
                for idx in range(1, len(q)):
                    tmp_answer = tmp_answer ^ q[idx]
                answer += tmp_answer
            
            for idx in range(pos, len(self.nums)):
                dfs(idx+1, q+[self.nums[idx]])

        dfs(0, [])
        return answer
        