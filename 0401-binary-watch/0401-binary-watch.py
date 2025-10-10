class Solution:
    answer = []

    def dfs(self, hour, minute, level, turnedOn, pos):
        if not ((0<=hour<=11) and (0<=minute<=59)):
            return
        
        if level == turnedOn:
            self.answer.append(f"{hour}:{minute:02d}")
            return

        for npos in range(pos, 10):
            if npos < 4:
                self.dfs(hour + 2**npos, minute, level+1, turnedOn, npos+1)
            else:
                self.dfs(hour, minute + 2**(npos-4), level+1, turnedOn, npos+1)

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.dfs(0, 0, 0, turnedOn, 0)
        answer = self.answer[:]
        self.answer.clear()
        return answer
