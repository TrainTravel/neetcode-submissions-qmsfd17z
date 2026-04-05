class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        
        # iterate through each course's prerequisites, cycle detected -> false
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[c].append(p)

        def dfs(course: int, path: Set[int]) -> bool:
            if course in path:
                return False
            if course in visited:
                return True

            # 1. Add current course to the current path
            path.add(course)

            # 2. Check all prerequisites
            for pre in adj_list[course]:
                if not dfs(pre, path):
                    return False
            
            # 3. backtrack
            path.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True