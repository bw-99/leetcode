# class Solution:
#     path = []
#     path_final = set()

#     def dfs(self, cur_item: int):
#         self.path.append(cur_item)

#         if (pre_course_list := self.prerequisites_dict.get(cur_item, None)) is None:
#             return True
         
#         for pre_course in pre_course_list:
#             is_visited = self.visited.get(pre_course, False)
            
#             if is_visited:
#                 return False

#             if pre_course in self.path_final:
#                 continue
            
#             self.visited[pre_course] = True
#             is_possible = self.dfs(pre_course)
#             self.visited[pre_course] = False

#             if not is_possible:
#                 return False
#         return True

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         self.path = []
#         self.path_final = set()

#         prerequisites_dict = {}
#         for item in prerequisites:
#             if item[0] in list(prerequisites_dict.keys()):
#                 prerequisites_dict[item[0]].append(item[1])
#             else:
#                 prerequisites_dict[item[0]] = [item[1]]
        
#         self.prerequisites_dict = prerequisites_dict
        
#         self.visited = {
#             i: False for i in range(numCourses)
#         }

#         dont_need_to_check = set()
        
#         answer = True
#         for course in list(prerequisites_dict.keys()):       

#             self.visited[course] = True
#             is_possible = self.dfs(course)
#             self.visited[course] = False

#             answer = answer and is_possible

#             if not answer:
#                 return False
            
#             self.path_final = set(self.path)
#             for course in self.path_final:
#                 self.visited[course] = None
#         return answer

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerequisites_dict: dict[int, set[int] | None] = {}

        for item in prerequisites:
            if item[0] in list(prerequisites_dict.keys()):
                prerequisites_dict[item[0]].add(item[1])
            else:
                prerequisites_dict[item[0]] = {item[1]}
        
        self.prerequisites_dict = prerequisites_dict
                
        answer = True
            
        queue = [
            course for course in range(numCourses) if len(self.prerequisites_dict.get(course, [])) == 0
        ]
        count = 0
        
        while queue:
            course = queue.pop(0)

            prereq_course_lst = self.prerequisites_dict.get(course, None)
            # print(course, prereq_course_lst)

            parents = []
            if not prereq_course_lst:
                # print(course)
                count+=1
                # dependency 제거
                for key in self.prerequisites_dict.keys():
                    if course in self.prerequisites_dict[key]:
                        parents.append(key)
                        self.prerequisites_dict[key].remove(course)
                # print("remove ", self.prerequisites_dict, "parents", parents)
            
            for parent_course in parents:
                if len(self.prerequisites_dict.get(parent_course, [])) == 0:
                    queue.append(parent_course)
        return count == numCourses