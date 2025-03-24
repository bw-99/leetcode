class Solution:
    def get_plaindrome(left: int, right: int, s:str):
        while True:
            left, right = left-1, right+1
            if left < 0 or right >= len(s) or s[left] != s[right]:
                left, right = left+1, right-1
                break
        return s[left: right+1]

    def longestPalindrome(self, s: str) -> str:
        
        max_plaindrome = s[0]
        for idx in range(0, len(s)):
            if (1 <= idx < len(s)-1) and s[idx-1] == s[idx+1]:
                left, right = idx-1, idx+1
                tmp_answer = Solution.get_plaindrome(left, right, s)
                if len(max_plaindrome) < len(tmp_answer):
                    max_plaindrome = tmp_answer

            if (0 <= idx < len(s)-1) and s[idx+1] == s[idx]:
                left, right = idx, idx+1
                tmp_answer = Solution.get_plaindrome(left, right, s)
                if len(max_plaindrome) < len(tmp_answer):
                    max_plaindrome = tmp_answer

            
        return max_plaindrome
