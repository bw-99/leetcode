class Solution:
    path = set()

    def dfs(self, visited_dict: dict[int, bool], cur_item: int):
        self.path.add(cur_item)

        if (pre_course_list := self.prerequisites_dict.get(cur_item, None)) is None:
            return True
         
        for pre_course in pre_course_list:
            is_visited = visited_dict.get(pre_course, False)
            
            if is_visited:
                return False

            if pre_course in self.path:
                continue
            
            visited_dict[pre_course] = True
            is_possible = self.dfs(visited_dict, pre_course)
            visited_dict[pre_course] = False

            if not is_possible:
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = set()

        prerequisites_dict = {}
        for item in prerequisites:
            if item[0] in list(prerequisites_dict.keys()):
                prerequisites_dict[item[0]].append(item[1])
            else:
                prerequisites_dict[item[0]] = [item[1]]
        
        self.prerequisites_dict = prerequisites_dict
        
        visited = {
            i: False for i in range(numCourses)
        }

        dont_need_to_check = set()
        
        answer = True
        for course in list(prerequisites_dict.keys()):       

            visited[course] = True
            is_possible = self.dfs(visited, course)
            visited[course] = False

            answer = answer and is_possible

            if not answer:
                return False
            
            for course in self.path:
                visited[course] = None
        return answer