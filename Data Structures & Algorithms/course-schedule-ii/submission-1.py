class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {_: [] for _ in range(numCourses)}
        result = []

        # basically prerequisites is an adjacency list(2D)
        for course, pre in prerequisites:
            preMap[course].append(pre)
        # print(preMap)

        visiting = set()  # Current DFS path
        visited = set()   # Fully processed courses

        def dfs(c: int) -> bool:
            # base cases
            if c in visiting:
                return False
            if c in visited:
                return True

            # Mark course as visiting
            visiting.add(c)
            # print(visiting)

            # start taking course(by visiting)
            for pre in preMap[c]:
                # print(f"start taking precourse {pre} of {c}")
                if not dfs(pre):
                    # print(f"cycle detected: {c} <-> {pre}")
                    return False
                
            # After taking each precourse of course c, move c to visited
            visiting.remove(c)
            visited.add(c)
            result.append(c)
            return True
        
        # Check all courses
        for course in range(numCourses):
            print(f"start visiting course: {course}")
            if not dfs(course):
                return []
        return result