class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []
        
        def dfs(parentheses, level, left_count):
            nonlocal n

            if (left_count > n) or (len(parentheses) - left_count > n):
                return

            if level == 2*n:
                stack_parentheses = []

                for unit in parentheses:
                    if stack_parentheses and stack_parentheses[-1] == "(" and unit == ")":
                        stack_parentheses.pop(-1)
                    else:
                        stack_parentheses.append(unit)
                
                if len(stack_parentheses) == 0:
                    answer.append(parentheses)
                return

            dfs(parentheses + "(", level+1, left_count+1)
            dfs(parentheses + ")", level+1, left_count)
        
        dfs("", 0, 0)
        return answer

                


