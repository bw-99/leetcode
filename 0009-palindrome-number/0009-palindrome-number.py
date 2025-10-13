class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        if len(x_str) == 1:
            return True

        stack = [item for item in x_str[:(len(x_str)//2)]]

        for item in x_str[((len(x_str)+ 1)//2):]:
            if item == stack[-1]:
                stack.pop(-1)

        return len(stack)==0