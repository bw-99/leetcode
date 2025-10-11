class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []

        # candidates = sorted(candidates, key=lambda x: -x)
        
        def dfs(level: int, residual: int, traces: list[int]):
            if level == len(candidates):
                if residual == 0:
                    result = []
                    for idx in range(len(traces)):
                        result.extend([candidates[idx]]*traces[idx])
                    answer.append(result)
                return
            
            divisor = residual // candidates[level]
            for quotient in range(divisor+1):
                dfs(level+1, residual - candidates[level]*quotient, traces + [quotient])

        dfs(0, target, [])

        return answer