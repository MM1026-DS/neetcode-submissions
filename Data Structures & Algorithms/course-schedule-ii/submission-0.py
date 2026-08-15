class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {course:[] for course in range(numCourses)}

        for coursepreq in prerequisites:
            prereqcou = coursepreq[1]
            course = coursepreq[0]
            graph[course].append(prereqcou)
        
        path = set() 
        visited = set() 
        result = []

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True  
            path.add(course)
            for preeq in graph[course]:
                if not dfs(preeq):
                    return False 
            path.remove(course)
            visited.add(course)
            result.append(course)
            return True

      
        for courses in range(numCourses):
            if not dfs(courses):
                return []
           
        return result

       