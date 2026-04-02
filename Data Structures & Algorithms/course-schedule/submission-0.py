from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Map each course to its dependents (Adjacency List)
        # 2. Track in-degree of each course
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # 3. Add courses with no prerequisites to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        finish_count = 0
        while queue:
            crs = queue.popleft()
            finish_count += 1
            
            # 4. "Take" the course and reduce in-degree of its neighbors
            for neighbor in adj[crs]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we finished all courses, no cycle exists
        return finish_count == numCourses