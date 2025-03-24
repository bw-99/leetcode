class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        prev_max = 0
        while left < right:
            cur_area = min(height[left], height[right]) * (right-left)
            prev_max = max(prev_max, cur_area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return prev_max
            

