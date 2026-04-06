class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited = set()
        in_degree = [0] * numCourses
        taken = 0
        
        # iterate through each course's prerequisites, cycle detected -> false
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[p].append(c)
            in_degree[c] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            curr_pre = queue.popleft()
            taken += 1

            for course in adj_list[curr_pre]:
                in_degree[course] -= 1
            
                # If all dependencies are satisfied, it's ready to be taken
                if in_degree[course] == 0:
                    queue.append(course)
        return taken == numCourses              
