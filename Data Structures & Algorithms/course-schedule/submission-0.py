class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course:[] for course in range(numCourses)}

        for pre in prerequisites:
            course = pre[0]
            precourse = pre[1]
            graph[course].append(precourse)


        path = set() 
        visited = set() 
        def dfs(course):
            if course in path:
                return False 
            if course in visited:
                return True 
            path.add(course)
            
            for preCourse in graph[course]:
                if not dfs(preCourse):
                    return False
            path.remove(course)
            visited.add(course)
            return True
            
        
        for course in range(numCourses):
            if not dfs(course):
                return False 
        return True
        