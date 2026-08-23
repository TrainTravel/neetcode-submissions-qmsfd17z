class UnionFind:
    
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.component_cnt = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if self.isSameComponent(x, y):
            return False
    
        if self.rank[root_x] >= self.rank[root_y]:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        else:
            self.parent[root_x] = root_y
        self.component_cnt -= 1
        return True     

    def getNumComponents(self) -> int:
        return self.component_cnt

            

