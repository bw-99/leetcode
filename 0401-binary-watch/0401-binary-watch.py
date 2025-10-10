class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []

        def backtrack(pos, leds_on, hour, minute):
            if not ((0<= hour <= 11) and (0<=minute<=59)):
                return
            
            if leds_on == turnedOn:
                result.append(f"{hour}:{'0'*(2-len(str(minute)))}{minute}")
                return
            
            for i in range(pos, 10):
                if i < 4:
                    backtrack(i+1, leds_on+1, hour + 2**i, minute)
                else:
                    k = i - 4
                    backtrack(i+1, leds_on+1, hour, minute + 2**k)

        backtrack(0, 0, 0, 0)
        return result