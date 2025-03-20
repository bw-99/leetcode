class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 1
        ch_pos = {s[left]: left}
        max_len = 1
        while right < len(s):
            prev_right_pos = ch_pos.get(s[right], None)
            if prev_right_pos == None:
                ch_pos[s[right]] = right
            else:
                for idx in range(left, prev_right_pos+1):
                    del ch_pos[s[idx]]
                left = prev_right_pos+1
                ch_pos[s[right]] = right

            max_len = max(max_len, len(ch_pos.keys()))
            right += 1

        return max_len